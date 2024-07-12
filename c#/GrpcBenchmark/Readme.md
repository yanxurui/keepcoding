This is a benchmark for Grpc.AspNetCore.

## GrpcGreeterServer
Start Kestrel by default. Alternatively, you can start Http.Sys which requires special setup for the cert.

## GrpcGreeterClient
A wrk-like benchmark tool. You can the payload size the server responds and how many concurrent connections to run, etc.

```
> dotnet C:\code\keepcoding\c#\GrpcBenchmark\GrpcGreeterClient\bin\Release\net8.0\GrpcGreeterClient.dll --help

GrpcGreeterClient 1.0.0+67cf74e652802bd71a98dd0b1d1a4304ff183593
Copyright (C) 2024 GrpcGreeterClient

  -U, --url           (Default: https://localhost:5000) Url to do load test against

  -R, --run           (Default: 3) Number of runs

  -D, --duration      (Default: 20) Duration (seconds) to run the test

  -T, --thread        (Default: 5) Count of threads

  -C, --connection    (Default: 80) Concurrent connections per thread.

  -S, --streaming     (Default: false) whether to call the streaming rpc.

  --maxSize           (Default: 1000000)

  --minSize           (Default: 10)

  --help              Display this help screen.

  --version           Display version information.
```

```
> dotnet C:\code\keepcoding\c#\GrpcBenchmark\GrpcGreeterClient\bin\Release\net8.0\GrpcGreeterClient.dll -U https://localhost:5001 -R 1 --maxSize 10

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
