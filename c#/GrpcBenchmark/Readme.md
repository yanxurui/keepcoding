This is a benchmark for Grpc.AspNetCore.

## GrpcGreeterServer
Start Kestrel by default. Alternatively, you can start Http.Sys which requires special setup for the cert.

## GrpcGreeterClient
A wrk-like benchmark tool. Basically, you can specify how many concurrent connections to run and the payload size the server responds.

```
dotnet C:\code\keepcoding\c#\GrpcBenchmark\GrpcGreeterClient\bin\Release\net8.0\GrpcGreeterClient.dll -U https://localhost:5001 -R 1 --maxSize 10
===================================
Round 1/1
===================================
Running 20s test @ https://localhost:5001 with size 10 bytes
5 threads and 80 connections
1604002 requests in 20s, 0.01GB read
Requests/sec: 80200
Average Latency: 4.99ms

Final results:
10, 80200, 4.99
```
