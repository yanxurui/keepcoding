use clap::Parser;
use futures::StreamExt;
use std::sync::Arc;
use std::time::{Duration, Instant};
use tokio::sync::RwLock;
use tonic::transport::Channel;

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
}

#[derive(Clone)]
struct Result {
    request_count: Arc<RwLock<u64>>,
    response_size: Arc<RwLock<u64>>,
    failed_count: Arc<RwLock<u64>>,
    latencies: Arc<RwLock<Vec<f64>>>,
    duration: f64,
}

impl Result {
    fn new(duration: f64) -> Self {
        Self {
            request_count: Arc::new(RwLock::new(0)),
            response_size: Arc::new(RwLock::new(0)),
            failed_count: Arc::new(RwLock::new(0)),
            latencies: Arc::new(RwLock::new(Vec::new())),
            duration,
        }
    }

    async fn add(&self, latency: f64, response_length: usize, failed: bool) {
        {
            let mut count = self.request_count.write().await;
            *count += 1;
        }
        
        if !failed {
            let mut size = self.response_size.write().await;
            *size += response_length as u64;
        } else {
            let mut failed = self.failed_count.write().await;
            *failed += 1;
        }

        let mut latencies = self.latencies.write().await;
        latencies.push(latency);
    }

    async fn get_stats(&self) -> (u64, u64, u64, Vec<f64>) {
        let request_count = *self.request_count.read().await;
        let response_size = *self.response_size.read().await;
        let failed_count = *self.failed_count.read().await;
        let latencies = self.latencies.read().await.clone();
        
        (request_count, response_size, failed_count, latencies)
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
            let request_for_stream = download_request.clone();
            let response = client.clone().download_stream(tonic::Request::new(
                futures::stream::once(async move { request_for_stream })
            )).await?;

            let mut stream = response.into_inner();

            if let Some(reply) = stream.next().await {
                reply?
            } else {
                continue;
            }
        } else {
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
        "Starting benchmark with {} threads, {} connections per thread, {} seconds duration",
        args.threads, args.connections, args.duration
    );

    let result = Result::new(args.duration as f64);
    let mut tasks = Vec::new();

    for _ in 0..args.threads {
        let args_clone = args.clone();
        let result_clone = result.clone();
        let task = tokio::spawn(run_thread(args_clone, result_clone));
        tasks.push(task);
    }

    for task in tasks {
        task.await??;
    }

    Ok(result)
}

fn print_results(result: &Result, run: u32) {
    let (request_count, response_size, failed_count, latencies) = futures::executor::block_on(result.get_stats());
    
    println!("\n=== Run {} Results ===", run);
    println!("Total Requests: {}", request_count);
    println!("Failed Requests: {}", failed_count);
    println!("Total Response Size: {} bytes", response_size);
    println!("Requests per Second: {}", result.requests_per_second(request_count));
    println!("Average Latency: {:.2} ms", result.average_latency(&latencies));
    println!("50th Percentile Latency: {:.2} ms", result.percentile_latency(&latencies, 0.5));
    println!("95th Percentile Latency: {:.2} ms", result.percentile_latency(&latencies, 0.95));
    println!("99th Percentile Latency: {:.2} ms", result.percentile_latency(&latencies, 0.99));
    
    let top_latencies = result.top_latencies(&latencies, 5);
    println!("Top 5 Latencies: {:?} ms", top_latencies);
}

#[tokio::main]
async fn main() -> std::result::Result<(), Box<dyn std::error::Error + Send + Sync>> {
    let mut args = Args::parse();
    
    // Set a default size for testing
    args.size = args.min_size;

    println!("gRPC Benchmark Client");
    println!("URL: {}", args.url);
    println!("Runs: {}", args.runs);
    println!("Duration: {} seconds", args.duration);
    println!("Threads: {}", args.threads);
    println!("Connections per thread: {}", args.connections);
    println!("Streaming: {}", args.streaming);
    println!("Payload size: {} bytes", args.size);

    for run in 1..=args.runs {
        println!("\nStarting run {} of {}", run, args.runs);
        
        let result = run_benchmark(&args).await?;
        print_results(&result, run);
    }

    println!("\nBenchmark completed!");
    Ok(())
} 