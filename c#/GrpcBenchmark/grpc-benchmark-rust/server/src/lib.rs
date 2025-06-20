pub mod greeter_service;

#[cfg(test)]
mod tests {
    use super::*;
    use proto::{DownloadRequest, HelloRequest, SleepRequest};
    use tonic::Request;

    #[tokio::test]
    async fn test_say_hello() {
        let service = crate::greeter_service::GreeterService::default();
        let request = Request::new(HelloRequest {
            name: "World".to_string(),
        });

        let response = service.say_hello(request).await.unwrap();
        assert_eq!(response.get_ref().message, "Hello World");
    }

    #[tokio::test]
    async fn test_download() {
        let service = crate::greeter_service::GreeterService::default();
        let request = Request::new(DownloadRequest { request_size: 100 });

        let response = service.download(request).await.unwrap();
        assert_eq!(response.get_ref().body.len(), 100);
    }

    #[tokio::test]
    async fn test_sleep() {
        let service = crate::greeter_service::GreeterService::default();
        let request = Request::new(SleepRequest { seconds: 0 });

        let response = service.sleep(request).await.unwrap();
        assert_eq!(response.get_ref(), &());
    }
} 