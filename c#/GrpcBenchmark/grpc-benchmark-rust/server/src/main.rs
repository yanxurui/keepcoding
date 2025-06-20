use clap::Parser;
use proto::GreeterServer;
use server::greeter_service::GreeterService;
use tonic::transport::Server;
use tracing::{info, warn};

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

    let addr = format!("[::]:{}", args.port).parse()?;
    let greeter = GreeterService::default();

    info!("gRPC server listening on {}", addr);

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