use clap::Parser;
use futures::StreamExt;
use indicatif::{ProgressBar, ProgressStyle};
use std::collections::HashMap;
use std::sync::Arc;
use std::sync::atomic::{AtomicU64, Ordering};
use std::time::{Duration, Instant};
use tokio::sync::RwLock;
use tonic::transport::Channel;
use std::cell::RefCell;
use std::thread_local;

// Include the generated proto code inline
tonic::include_proto!("greet");

// Import the generated types
use crate::greeter_client::GreeterClient;

#[derive(Parser, Clone)]
#[command(author, version, about, long_about = None)]
struct Args {
    /// URL to do load test against
    #[arg(short, long, default_value = "http://localhost:5001")]
    url: String,

    /// Number of runs
    #[arg(short, long, default_value_t = 3)]
    runs: u32,

    /// Duration (seconds) to run the test
    #[arg(short, long, default_value_t = 20)]
    duration: u64,

    /// Count of threads
    #[arg(short, long, default_value_t = 5)]
    threads: u32,

    /// Concurrent connections per thread
    #[arg(short, long, default_value_t = 80)]
    connections: u32,

    /// Whether to call the streaming RPC
    #[arg(short, long)]
    streaming: bool,

    /// Maximum payload size
    #[arg(long, default_value_t = 1_000_000)]
    max_size: u32,

    /// Minimum payload size
    #[arg(long, default_value_t = 10)]
    min_size: u32,

    /// Current payload size for testing
    #[arg(skip)]
    size: u32,

    /// High performance mode - disable latency collection for max throughput
    #[arg(long)]
    high_perf: bool,
}

// Thread-local storage for latencies
thread_local! {
    static THREAD_LATENCIES: RefCell<Vec<f64>> = RefCell::new(Vec::new());
}

#[derive(Clone)]
struct Result {
    request_count: Arc<AtomicU64>,
    response_size: Arc<AtomicU64>,
    failed_count: Arc<AtomicU64>,
    latencies: Arc<RwLock<Vec<f64>>>,
    duration: f64,
    high_perf: bool,
}

impl Result {
    fn new(duration: f64, high_perf: bool) -> Self {
        Self {
            request_count: Arc::new(AtomicU64::new(0)),
            response_size: Arc::new(AtomicU64::new(0)),
            failed_count: Arc::new(AtomicU64::new(0)),
            latencies: Arc::new(RwLock::new(Vec::new())),
            duration,
            high_perf,
        }
    }

    async fn add(&self, latency: f64, response_length: usize, failed: bool) {
        // Use atomic operations - no locks needed!
        self.request_count.fetch_add(1, Ordering::Relaxed);

        if !failed {
            self.response_size.fetch_add(response_length as u64, Ordering::Relaxed);
        } else {
            self.failed_count.fetch_add(1, Ordering::Relaxed);
        }

        // Store latency in thread-local storage - no locks!
        if !self.high_perf {
            THREAD_LATENCIES.with(|latencies| {
                latencies.borrow_mut().push(latency);
            });
        }
    }

    async fn get_stats(&self) -> (u64, u64, u64, Vec<f64>) {
        // Atomic reads - no locks needed!
        let request_count = self.request_count.load(Ordering::Relaxed);
        let response_size = self.response_size.load(Ordering::Relaxed);
        let failed_count = self.failed_count.load(Ordering::Relaxed);
        
        // Collect latencies from all threads
        let latencies = if self.high_perf {
            Vec::new()
        } else {
            self.collect_all_latencies().await
        };

        (request_count, response_size, failed_count, latencies)
    }

    async fn collect_all_latencies(&self) -> Vec<f64> {
        // This is called only once at the end, so locking is acceptable
        let mut all_latencies = Vec::new();
        
        // Collect from thread-local storage
        THREAD_LATENCIES.with(|latencies| {
            let mut thread_latencies = latencies.borrow_mut();
            all_latencies.append(&mut *thread_latencies);
        });

        all_latencies
    }

    fn requests_per_second(&self, request_count: u64) -> u64 {
        (request_count as f64 / self.duration) as u64
    }

    fn average_latency(&self, latencies: &[f64]) -> f64 {
        if latencies.is_empty() {
            0.0
        } else {
            latencies.iter().sum::<f64>() / latencies.len() as f64
        }
    }

    fn percentile_latency(&self, latencies: &[f64], percentile: f64) -> f64 {
        if latencies.is_empty() {
            return 0.0;
        }

        let mut sorted = latencies.to_vec();
        sorted.sort_by(|a, b| a.partial_cmp(b).unwrap());

        let index = ((percentile * sorted.len() as f64) - 1.0).max(0.0) as usize;
        sorted[index.min(sorted.len() - 1)]
    }

    fn top_latencies(&self, latencies: &[f64], count: usize) -> Vec<f64> {
        let mut sorted = latencies.to_vec();
        sorted.sort_by(|a, b| b.partial_cmp(a).unwrap());
        sorted.into_iter().take(count).collect()
    }
}

async fn create_channel(url: &str) -> std::result::Result<Channel, Box<dyn std::error::Error + Send + Sync>> {
    let channel = Channel::from_shared(url.to_string())?
        .connect()
        .await?;
    Ok(channel)
}

async fn run_connection(
    client: GreeterClient<Channel>,
    args: Args,
    result: Result,
) -> std::result::Result<(), Box<dyn std::error::Error + Send + Sync>> {
    // Create the inner request once and reuse it
    let download_request = DownloadRequest {
        request_size: args.size,
    };

    let start = Instant::now();
    let duration = Duration::from_secs(args.duration);

    while start.elapsed() < duration {
        let request_start = Instant::now();

        let response = if args.streaming {
            // For streaming, we'll use a simple approach
            // In a real implementation, you might want to maintain the stream
            let response = client.clone().download_stream(tonic::Request::new(
                futures::stream::once(async move { download_request.clone() })
            )).await?;

            let mut stream = response.into_inner();

            if let Some(reply) = stream.next().await {
                reply?
            } else {
                continue;
            }
        } else {
            // Create the tonic request inside the loop - this is actually more efficient
            client.clone().download(tonic::Request::new(download_request.clone())).await?.into_inner()
        };

        let latency = request_start.elapsed().as_micros() as f64 / 1000.0;
        let response_length = response.body.len();
        
        result.add(latency, response_length, false).await;
    }

    Ok(())
}

async fn run_thread(args: Args, result: Result) -> std::result::Result<(), Box<dyn std::error::Error + Send + Sync>> {
    let mut tasks = Vec::new();
    let channel = create_channel(&args.url).await?;

    for _ in 0..args.connections {
        let client = GreeterClient::new(channel.clone());
        let args_clone = args.clone();
        let result_clone = result.clone();
        let task = tokio::spawn(run_connection(client, args_clone, result_clone));
        tasks.push(task);
    }

    for task in tasks {
        task.await??;
    }

    Ok(())
}

async fn run_benchmark(args: &Args) -> std::result::Result<Result, Box<dyn std::error::Error + Send + Sync>> {
    println!(
        "Running {}s test @ {} with size {} bytes",
        args.duration, args.url, args.size
    );
    println!("{} threads and {} connections", args.threads, args.connections);

    let result = Result::new(args.duration as f64, args.high_perf);
    let mut tasks = Vec::new();

    for _ in 0..args.threads {
        let task = tokio::spawn(run_thread(args.clone(), result.clone()));
        tasks.push(task);
    }

    // Progress bar
    let pb = ProgressBar::new(args.duration);
    pb.set_style(
        ProgressStyle::default_bar()
            .template("{spinner:.green} [{elapsed_precise}] [{bar:40.cyan/blue}] {pos}/{len} ({eta}) {msg}")
            .unwrap()
            .progress_chars("#>-"),
    );

    let mut last_count = 0;
    for _i in 0..args.duration {
        tokio::time::sleep(Duration::from_secs(1)).await;
        
        // Use atomic read - much faster than get_stats()
        let current_count = result.request_count.load(std::sync::atomic::Ordering::Relaxed);
        let qps = current_count - last_count;
        pb.set_message(format!("Payload: {}, QPS: {} reqs/sec", args.size, qps));
        pb.inc(1);
        last_count = current_count;
    }

    // Wait for all tasks to complete
    for task in tasks {
        task.await??;
    }

    print_results(&result);

    Ok(result)
}

fn print_results(result: &Result) {
    let (request_count, response_size, failed_count, latencies) = futures::executor::block_on(result.get_stats());

    println!(
        "{} requests in {}s, {:.2}GB read",
        request_count,
        result.duration,
        response_size as f64 / (1 << 30) as f64
    );

    if failed_count > 0 {
        println!("Failed Requests: {}", failed_count);
    }

    println!("Requests/sec: {}", result.requests_per_second(request_count));
    
    if !result.high_perf && !latencies.is_empty() {
        println!("Average Latency: {:.2}ms", result.average_latency(&latencies));
        println!("P95 Latency: {:.2}ms", result.percentile_latency(&latencies, 0.95));
        println!("P99 Latency: {:.2}ms", result.percentile_latency(&latencies, 0.99));

        println!("Top 5 Latencies:");
        for latency in result.top_latencies(&latencies, 5) {
            println!("{:.2}", latency);
        }
    } else if result.high_perf {
        println!("Latency statistics disabled in high-performance mode");
    }
}

#[tokio::main]
async fn main() -> std::result::Result<(), Box<dyn std::error::Error + Send + Sync>> {
    let mut args = Args::parse();
    let mut results: HashMap<u32, Vec<Result>> = HashMap::new();

    for i in 0..args.runs {
        println!("===================================");
        println!("Round {}/{}", i + 1, args.runs);
        println!("===================================");

        // Generate logarithmic steps: 10, 100, 1000, 10000, 100000, 1000000
        let mut size = args.min_size;
        while size <= args.max_size {
            args.size = size; // Modify in place instead of cloning

            let result = run_benchmark(&args).await?;
            
            results.entry(size).or_insert_with(Vec::new).push(result);

            println!();
            tokio::time::sleep(Duration::from_secs(2)).await;

            // Multiply by 10 for next iteration
            size *= 10;
        }
    }

    println!("Final results:");
    let mut size = args.min_size;
    while size <= args.max_size {
        if let Some(run_results) = results.get(&size) {
            let mut requests_per_second: Vec<u64> = run_results
                .iter()
                .map(|r| {
                    let (count, _, _, _) = futures::executor::block_on(r.get_stats());
                    r.requests_per_second(count)
                })
                .collect();
            
            requests_per_second.sort();
            let median_rps = requests_per_second[requests_per_second.len() / 2];

            let mut avg_latencies: Vec<f64> = run_results
                .iter()
                .map(|r| {
                    let (_, _, _, latencies) = futures::executor::block_on(r.get_stats());
                    r.average_latency(&latencies)
                })
                .collect();
            
            avg_latencies.sort_by(|a, b| a.partial_cmp(b).unwrap());
            let median_latency = avg_latencies[avg_latencies.len() / 2];

            println!("{}, {}, {:.2}", size, median_rps, median_latency);
        }
        size *= 10;
    }
    Ok(())
} 