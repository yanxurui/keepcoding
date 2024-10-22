using GrpcGreeter.Services;
using Microsoft.AspNetCore.Http.Features;
using Microsoft.AspNetCore.Server.Kestrel.Core;
using System.IO.Pipelines;

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
        options.UrlPrefixes.Add("https://+:5002/");
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

//Http.sys only
//app.Use((c, n) =>
//{
//    var prev = c.Features.GetRequiredFeature<IHttpResponseBodyFeature>();
//    prev.Writer.GetType().GetField("_minimumBufferSize", System.Reflection.BindingFlags.NonPublic | System.Reflection.BindingFlags.Instance).SetValue(prev.Writer, 102400);
//    return n(c);
//});

// Configure the HTTP request pipeline.
app.MapGrpcService<GreeterService>();
app.MapGet("/", () => "Communication with gRPC endpoints must be made through a gRPC client. To learn how to create a client, visit: https://go.microsoft.com/fwlink/?linkid=2086909");

app.Run();

class CustomPipeWriterService : IHttpResponseBodyFeature
{
    private readonly IHttpResponseBodyFeature _prev;
    private readonly PipeWriter _writer;

    public CustomPipeWriterService(IHttpResponseBodyFeature prev)
    {
        _prev = prev;
        // Change 8192 here to test larger buffer sizes for impact
        _writer = PipeWriter.Create(_prev.Stream, new StreamPipeWriterOptions(minimumBufferSize: 8192, leaveOpen: true));
    }

    public Stream Stream => _prev.Stream;

    public PipeWriter Writer => _writer;

    public async Task CompleteAsync()
    {
        await _writer.CompleteAsync();
        await _prev.CompleteAsync();
    }

    public void DisableBuffering()
    {
        _prev.DisableBuffering();
    }

    public Task SendFileAsync(string path, long offset, long? count, CancellationToken cancellationToken = default)
    {
        return _prev.SendFileAsync(path, offset, count, cancellationToken);
    }

    public Task StartAsync(CancellationToken cancellationToken = default)
    {
        return _prev.StartAsync(cancellationToken);
    }
}