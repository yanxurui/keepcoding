$benchmarkArgs = @(
    "--proto=./proto/greet.proto",
    "--call=greet.Greeter.Download",
    "--disable-template-functions",
    "--disable-template-data",
    "--insecure",
    "--concurrency=1000",
    "--connections=50",
    "--rps=0",
    "--duration", "10s",
    "--data", '{"requestSize": 100}',
    "localhost:5001"
)

ghz @benchmarkArgs