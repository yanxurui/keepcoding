using GrpcGreeter.Services;
using Microsoft.AspNetCore.Server.Kestrel.Core;

var builder = WebApplication.CreateBuilder(args);
bool useHttpSys = false;
if (args.Length > 0)
{
    useHttpSys = args[0] == "httpsys";
}

if (useHttpSys)
{

#pragma warning disable CA1416 // Validate platform compatibility
    builder.WebHost.UseHttpSys(options =>
    {
        options.MaxRequestBodySize = 30_000_000;
        options.UrlPrefixes.Add("https://*:5002");
        options.EnableKernelResponseBuffering = true;
    });
#pragma warning restore CA1416 // Validate platform compatibility
}
else
{
    var socketPath = Path.Combine(Path.GetTempPath(), "greeter.tmp");
    var pipeName = "PipeGreeter";

    builder.WebHost.ConfigureKestrel(serverOptions =>
    {
        serverOptions.ListenAnyIP(5001, listenOptions =>
        {
            listenOptions.UseHttps();
            listenOptions.Protocols = HttpProtocols.Http2;
        });
        serverOptions.ListenUnixSocket(socketPath, listenOptions =>
        {
            listenOptions.Protocols = HttpProtocols.Http2;
        });
        serverOptions.ListenNamedPipe(pipeName, listenOptions =>
        {
            listenOptions.Protocols = HttpProtocols.Http2;
        });
    });
}


// Add services to the container.
builder.Services.AddGrpc();

var app = builder.Build();

// Configure the HTTP request pipeline.
app.MapGrpcService<GreeterService>();
app.MapGet("/", () => "Communication with gRPC endpoints must be made through a gRPC client. To learn how to create a client, visit: https://go.microsoft.com/fwlink/?linkid=2086909");

app.Run();
