use clap::Parser;
use std::collections::HashMap;
use tonic::transport::Server;
use tokio_stream::wrappers::ReceiverStream;
use tonic::{Request, Response, Status};
use tracing::{info, warn};

// Include the generated proto code inline
tonic::include_proto!("greet");

// Import the generated types
use crate::greeter_server::{Greeter, GreeterServer};

#[derive(Default)]
pub struct GreeterService {
    response_map: HashMap<u32, Vec<u8>>,
}

impl GreeterService {
    fn new() -> Self {
        let mut response_map = HashMap::new();

        // Pre-allocate all required sizes: 10, 100, 1000, 10000, 100000, 1000000
        let sizes = vec![10, 100, 1000, 10000, 100000, 1000000];

        for size in sizes {
            response_map.insert(size, vec![0u8; size as usize]);
        }

        Self {
            response_map,
        }
    }

    fn get_byte_string(&self, size: u32) -> Vec<u8> {
        self.response_map.get(&size)
            .cloned()
            .unwrap_or_else(|| vec![0u8; size as usize])
    }
}

#[tonic::async_trait]
impl Greeter for GreeterService {
    async fn say_hello(
        &self,
        request: Request<HelloRequest>,
    ) -> Result<Response<HelloReply>, Status> {
        let name = request.into_inner().name;
        let reply = HelloReply {
            message: format!("Hello {}", name),
        };
        Ok(Response::new(reply))
    }

    async fn download(
        &self,
        request: Request<DownloadRequest>,
    ) -> Result<Response<DownloadReply>, Status> {
        let request_size = request.into_inner().request_size;
        let body = self.get_byte_string(request_size);

        let reply = DownloadReply { body };
        Ok(Response::new(reply))
    }

    type DownloadStreamStream = ReceiverStream<Result<DownloadReply, Status>>;

    async fn download_stream(
        &self,
        request: Request<tonic::Streaming<DownloadRequest>>,
    ) -> Result<Response<Self::DownloadStreamStream>, Status> {
        let mut stream = request.into_inner();
        let (tx, rx) = tokio::sync::mpsc::channel(128);

        tokio::spawn(async move {
            while let Some(request) = stream.message().await.unwrap_or(None) {
                let request_size = request.request_size;
                let body = vec![0u8; request_size as usize];

                let reply = DownloadReply { body };
                if tx.send(Ok(reply)).await.is_err() {
                    break;
                }
            }
        });

        Ok(Response::new(ReceiverStream::new(rx)))
    }

    async fn sleep(
        &self,
        request: Request<SleepRequest>,
    ) -> Result<Response<()>, Status> {
        let seconds = request.into_inner().seconds;

        // Use sleep to mimic blocking operation
        tokio::time::sleep(tokio::time::Duration::from_secs(seconds as u64)).await;

        let thread_id = std::thread::current().id();
        info!("Thread id: {:?}", thread_id);

        Ok(Response::new(()))
    }
}

#[derive(Parser)]
#[command(author, version, about, long_about = None)]
struct Args {
    /// Port to listen on
    #[arg(short, long, default_value_t = 5001)]
    port: u16,

    /// Use HTTP instead of HTTPS
    #[arg(long)]
    http: bool,
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let args = Args::parse();

    // Initialize tracing
    tracing_subscriber::fmt::init();

    let addr = format!("[::1]:{}", args.port).parse()?;
    let greeter = GreeterService::new();

    println!("GreeterServer listening on {}", addr);

    if args.http {
        Server::builder()
            .add_service(GreeterServer::new(greeter))
            .serve(addr)
            .await?;
    } else {
        // For HTTPS, you would need to configure TLS certificates
        // This is a simplified version without TLS
        warn!("Running without TLS - use --http flag for HTTP or configure TLS certificates");
        Server::builder()
            .add_service(GreeterServer::new(greeter))
            .serve(addr)
            .await?;
    }

    Ok(())
} 