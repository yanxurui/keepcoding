#[cfg(test)]
mod tests {
    use tonic::Request;
    use crate::greeter_client::GreeterClient;
    use crate::{HelloRequest, DownloadRequest, SleepRequest};

    async fn create_test_client() -> GreeterClient<tonic::transport::Channel> {
        let server_url = "http://[::1]:5001"; // Assume server is running on default port
        GreeterClient::connect(server_url).await.unwrap()
    }

    #[tokio::test]
    async fn test_say_hello_e2e() {
        let mut client = create_test_client().await;

        let request = Request::new(HelloRequest {
            name: "World".to_string(),
        });

        let response = client.say_hello(request).await.unwrap();
        assert_eq!(response.get_ref().message, "Hello World");
    }

    #[tokio::test]
    async fn test_download_e2e() {
        let mut client = create_test_client().await;

        let request = Request::new(DownloadRequest { request_size: 100 });

        let response = client.download(request).await.unwrap();
        assert_eq!(response.get_ref().body.len(), 100);
    }

    #[tokio::test]
    async fn test_sleep_e2e() {
        let mut client = create_test_client().await;

        let request = Request::new(SleepRequest { seconds: 0 });

        let response = client.sleep(request).await.unwrap();
        assert_eq!(response.get_ref(), &());
    }

    #[tokio::test]
    async fn test_multiple_requests_e2e() {
        let mut client = create_test_client().await;

        // Test multiple requests to ensure server handles them correctly
        for i in 0..5 {
            let request = Request::new(HelloRequest {
                name: format!("User{}", i),
            });

            let response = client.say_hello(request).await.unwrap();
            assert_eq!(response.get_ref().message, format!("Hello User{}", i));
        }
    }

    #[tokio::test]
    async fn test_different_payload_sizes_e2e() {
        let mut client = create_test_client().await;

        let sizes = vec![10, 100, 1000, 10000];

        for size in sizes {
            let request = Request::new(DownloadRequest { request_size: size });

            let response = client.download(request).await.unwrap();
            assert_eq!(response.get_ref().body.len(), size as usize);
        }
    }
} 