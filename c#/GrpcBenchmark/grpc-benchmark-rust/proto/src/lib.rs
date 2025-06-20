pub mod greet {
    tonic::include_proto!("greet");
}

pub use greet::greeter_server::{Greeter, GreeterServer};
pub use greet::{DownloadReply, DownloadRequest, HelloReply, HelloRequest, SleepRequest}; 