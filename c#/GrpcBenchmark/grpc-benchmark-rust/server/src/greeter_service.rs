use proto::{DownloadReply, DownloadRequest, Greeter, HelloReply, HelloRequest, SleepRequest};
use std::collections::HashMap;
use std::sync::Arc;
use tokio::sync::RwLock;
use tonic::{Request, Response, Status};
use tracing::info;

#[derive(Default)]
pub struct GreeterService {
    response_map: Arc<RwLock<HashMap<u32, Vec<u8>>>>,
}

impl GreeterService {
    async fn get_byte_string(&self, size: u32) -> Vec<u8> {
        let mut map = self.response_map.write().await;
        
        if let Some(bytes) = map.get(&size) {
            bytes.clone()
        } else {
            let bytes = vec![0u8; size as usize];
            map.insert(size, bytes.clone());
            bytes
        }
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
        let body = self.get_byte_string(request_size).await;
        
        let reply = DownloadReply { body };
        Ok(Response::new(reply))
    }

    type DownloadStreamStream = tonic::codec::Streaming<DownloadReply>;

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

        Ok(Response::new(tonic::codec::Streaming::new(rx)))
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