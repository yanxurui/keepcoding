# gRPC Benchmark Tool in Rust

This is a high-performance gRPC benchmark tool written in Rust using Tonic. It provides both a server and client for benchmarking gRPC performance with various payload sizes and concurrency levels.

## Features

- **High-performance gRPC server** using Tonic
- **Benchmark client** with configurable parameters
- **Multiple RPC types**: Unary, Server Streaming, and Sleep operations
- **Configurable payload sizes** from 10 bytes to 1MB
- **Concurrent connection testing** with multiple threads
- **Detailed statistics** including latency percentiles and throughput
- **Progress tracking** with real-time QPS display

## Project Structure

```
grpc-benchmark-rust/
├── Cargo.toml              # Workspace configuration
├── proto/                  # Protocol buffer definitions
│   ├── Cargo.toml
│   ├── build.rs
│   ├── proto/greet.proto   # gRPC service definition
│   └── src/lib.rs
├── server/                 # gRPC server implementation
│   ├── Cargo.toml
│   └── src/main.rs
└── client/                 # Benchmark client
    ├── Cargo.toml
    └── src/main.rs
```

## Prerequisites

- Rust 1.70+ and Cargo
- Protocol Buffers compiler (protoc)

### Installing Rust

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source ~/.cargo/env
```

**Windows:**
Download rustup-init.exe from https://www.rust-lang.org/tools/install


### Installing Protocol Buffers

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install protobuf-compiler
```

**macOS:**
```bash
brew install protobuf
```

**Windows:**
Download from https://github.com/protocolbuffers/protobuf/releases
```
1. Extract protoc-31.1-win64.zip to a folder (e.g., C:\protoc)
2. Add the bin folder to your PATH environment variable:
   - Open System Properties > Advanced > Environment Variables
   - Edit the PATH variable and add: C:\protoc\bin
3. Verify installation: protoc --version
```

## Building

```bash
# Clone the repository
git clone <repository-url>
cd grpc-benchmark-rust

# Build all crates
cargo build --release
```


## Usage

### Starting the Server

```bash
# Start server on default port 5001
cargo run --release --bin server

# Start server on custom port
cargo run --release --bin server -- --port 5002

# Start server with HTTP (no TLS)
cargo run --release --bin server -- --http
```

### Running Benchmarks

```bash
# Basic benchmark with default settings
cargo run --release --bin client

# Custom benchmark parameters
cargo run --release --bin client -- \
  --url http://localhost:5001 \
  --duration 30 \
  --threads 10 \
  --connections 100 \
  --min-size 100 \
  --max-size 10000

# Streaming benchmark
cargo run --release --bin client -- --streaming

# Single run with specific payload size
cargo run --release --bin client -- \
  --runs 1 \
  --max-size 1000 \
  --min-size 1000
```

## Command Line Options

### Server Options

- `-p, --port <PORT>`: Port to listen on (default: 5001)
- `--http`: Use HTTP instead of HTTPS (no TLS)

### Client Options

- `-U, --url <URL>`: URL to test against (default: http://localhost:5001)
- `-R, --runs <RUNS>`: Number of benchmark runs (default: 3)
- `-D, --duration <SECONDS>`: Duration of each test in seconds (default: 20)
- `-T, --thread <THREADS>`: Number of threads (default: 5)
- `-C, --connection <CONNECTIONS>`: Concurrent connections per thread (default: 80)
- `-S, --streaming`: Use streaming RPC instead of unary
- `--max-size <BYTES>`: Maximum payload size (default: 1,000,000)
- `--min-size <BYTES>`: Minimum payload size (default: 10)

## Example Output

```
===================================
Round 1/3
===================================
Running 20s test @ http://localhost:5001 with size 10 bytes
5 threads and 80 connections
[████████████████████████████████████████] 20/20 (0s remaining)
1604002 requests in 20s, 0.01GB read
Requests/sec: 80200
Average Latency: 4.99ms
P95 Latency: 8.45ms
P99 Latency: 12.34ms
Top 5 Latencies:
15.67
14.23
13.89
13.45
12.98

Final results:
10, 80200, 4.99
100, 45600, 8.76
1000, 12300, 32.45
```

## Performance Characteristics

The Rust implementation using Tonic provides:

- **High throughput**: Optimized for maximum requests per second
- **Low latency**: Minimal overhead for request processing
- **Memory efficiency**: Efficient memory usage with zero-copy operations
- **Concurrent processing**: Async/await based concurrency model
- **Connection pooling**: Reuse of gRPC channels for better performance

## Comparison with C# Implementation

This Rust version maintains feature parity with the original C# implementation while providing:

- **Better performance**: Rust's zero-cost abstractions and memory safety
- **Lower resource usage**: More efficient memory and CPU utilization
- **Cross-platform**: Native compilation for all major platforms
- **Type safety**: Compile-time guarantees for better reliability

## Development

### Adding New RPC Methods

1. Update `proto/proto/greet.proto` with new service definitions
2. Rebuild the proto crate: `cargo build -p proto`
3. Implement the new methods in `server/src/main.rs`
4. Add client calls in `client/src/main.rs`

### Running Tests

```bash
# Run all tests
cargo test

# Run tests for specific crate
cargo test -p server
cargo test -p client
```

## License

MIT License - see LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Troubleshooting

### Common Issues

**Build fails with protobuf errors:**
- Ensure `protoc` is installed and in your PATH
- Check that the protobuf version is compatible (3.0+)

**Connection refused errors:**
- Verify the server is running on the expected port
- Check firewall settings
- Use `--http` flag if TLS certificates are not configured

**Performance issues:**
- Ensure you're using `--release` builds for benchmarking
- Adjust thread and connection counts based on your system
- Monitor system resources during testing 