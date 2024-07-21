// This is a wrk like gRpc benchmarking tool written in C#
using CommandLine;
using Google.Protobuf.WellKnownTypes;
using Grpc.Core;
using Grpc.Net.Client;
using Greet;
using System.Collections.Concurrent;
using System.Diagnostics;
using System.IO.Pipes;
using System.Net;
using System.Net.Sockets;
using System.Security.Principal;
using ShellProgressBar;


await Main(args);

async Task Main(string[] args)
{
    var o = Parser.Default.ParseArguments<Options>(args).Value;

    if (o == null)
    {
        return;
    }

    Dictionary<int, Result[]> results = new Dictionary<int, Result[]>();
    for (int i = 0; i < o.Runs; i++)
    {
        Console.WriteLine("===================================");
        Console.WriteLine("Round {0}/{1}", i + 1, o.Runs);
        Console.WriteLine("===================================");
        for (int size = o.MinSize; size <= o.MaxSize; size *= 10)
        {
            o.Size = size;
            Result r = await Run(o);
            if (!results.ContainsKey(size))
            {
                results.Add(size, new Result[o.Runs]);
            }

            results[size][i] = r;

            // print a blank line between runs
            Console.WriteLine();

            // sleep for 2 seconds between runs
            await Task.Delay(2000);
        }
    }


    Console.WriteLine("Final results:");
    for (int size = o.MinSize; size <= o.MaxSize; size *= 10)
    {
        // Get the median of all runs
        var median = results[size].OrderBy(r => r.RequestPerSecond).ElementAt(o.Runs / 2);

        // Console.WriteLine("Size: {0}B, Requests/sec: {1}, Average Latency: {2:F2}ms", size, median.RequestPerSecond, median.AverageLatency);
        // print in csv format
        Console.WriteLine("{0}, {1}, {2:F2}", size, median.RequestPerSecond, median.AverageLatency);
    }
}

async Task<Result> Run(Options o)
{
    Console.WriteLine("Running {0}s test @ {1} with size {2} bytes", o.Duration, o.Url, o.Size);
    Console.WriteLine("{0} threads and {1} connections", o.Threads, o.Connections);

    Result result = new Result();
    result.Duration = o.Duration;

    var tasks = new List<Task>();

    for (int i = 0; i < o.Threads; i++)
    {
        // Use Task.Run) to run the task in a seperate thread
        tasks.Add(Task.Run(() => RunThread(o, result)));
    }

    var waitingTask = Task.WhenAll(tasks);

    var totalTicks = o.Duration;
    var options = new ProgressBarOptions
    {
        ProgressCharacter = '─',
    };
    using (var pbar = new ProgressBar(totalTicks, "benchmark...", options))
    {
        int lastCount = 0;
        int currentCount;
        while (false == waitingTask.IsCompleted)
        {
            // wait for 1 second
            await Task.Delay(1000);
            // will advance pbar to 1 out of totalTicks.
            // also advance and update the progressbar text
            currentCount = result.Latencies.Count;
            pbar.Tick($"QPS: {currentCount-lastCount} reqs/sec");
            lastCount = currentCount;
        }
    }

    // await Task.WhenAll(tasks);

    // Print stats
    Console.WriteLine("{0} requests in {1}s, {2:F2}GB read", result.RequestCount, result.Duration, 1.0 * result.ResponseSize / (1 << 30));
    if (result.FailedRequests.Count > 0)
    {
        Console.WriteLine("Non-2xx or 3xx responses: {0}", result.FailedRequests.Count);
    }
    Console.WriteLine("Requests/sec: {0}", result.RequestPerSecond);
    Console.WriteLine("Average Latency: {0:F2}ms", result.AverageLatency);

    return result;
}

async Task RunThread(Options o, Result result)
{
    var tasks = new List<Task>();
    var channel = CreateChannel(o.Url);
    var client = new Greeter.GreeterClient(channel);
    for (int i = 0; i < o.Connections; i++)
    {
        tasks.Add(RunConnection(client, o, result));
    }

    await Task.WhenAll(tasks);
    await channel.ShutdownAsync();
}

async Task RunConnection(Greeter.GreeterClient client, Options o, Result result)
{
    double t;
    DownloadRequest downloadRequest = new DownloadRequest { RequestSize = (uint)o.Size };
    DownloadReply reply;
    var sw = Stopwatch.StartNew();
    while (sw.Elapsed.TotalSeconds < o.Duration)
    {
        t = sw.Elapsed.TotalMilliseconds;

        /**********************************************/
        // to mimic creating a new channel for each request
        /**********************************************/
        // var channel = CreateChannel(o.Url);
        // client = new Greeter.GreeterClient(channel);

        if (o.Streaming)
        {
            // the using ensures it's always disposed if an unexpected error occurs.
            using var stream = client.DownloadStream();
            reply = await DoRequestStream(client, stream, downloadRequest);
        }
        else
        {
            reply = await DoRequest(client, downloadRequest);
        }

        // await channel.ShutdownAsync();

        result.Add(sw.Elapsed.TotalMilliseconds - t, reply.Body.Length);
    }
}

async Task<DownloadReply> DoRequest(Greeter.GreeterClient client, DownloadRequest downloadRequest)
{
    return await client.DownloadAsync(downloadRequest);
}

async Task<DownloadReply> DoRequestStream(Greeter.GreeterClient client, AsyncDuplexStreamingCall<DownloadRequest, DownloadReply> stream, DownloadRequest downloadRequest)
{
    // stream = client.DownloadStream();
    await stream.RequestStream.WriteAsync(downloadRequest);
    await stream.RequestStream.CompleteAsync();

    await stream.ResponseStream.MoveNext();

    return stream.ResponseStream.Current;
}

GrpcChannel CreateChannel(string address)
{
    if (address.StartsWith("http"))
    {
        return GrpcChannel.ForAddress(address);
    }
    else if (address.StartsWith("unix:"))
    {
        string socketPath = address.Substring(5);

        var udsEndPoint = new UnixDomainSocketEndPoint(socketPath);
        var connectionFactory = new UnixDomainSocketsConnectionFactory(udsEndPoint);
        var socketsHttpHandler = new SocketsHttpHandler
        {
            ConnectCallback = connectionFactory.ConnectAsync
        };

        return GrpcChannel.ForAddress("http://localhost", new GrpcChannelOptions
        {
            HttpHandler = socketsHttpHandler
        });
    }
    else if (address.StartsWith("pipe:"))
    {
        string pipeName = address.Substring(5);
        var connectionFactory = new NamedPipesConnectionFactory(pipeName);
        var socketsHttpHandler = new SocketsHttpHandler
        {
            ConnectCallback = connectionFactory.ConnectAsync
        };

        return GrpcChannel.ForAddress("http://localhost", new GrpcChannelOptions
        {
            HttpHandler = socketsHttpHandler
        });
    }
    else
    {
        throw new ArgumentException("Invalid Url");
    }
}

public class Result
{
    public double Duration { get; set; }

    public int RequestPerSecond
    {
        get
        {
            return (int)(requestCount / Duration);
        }
    }

    public double AverageLatency
    {
        get
        {
            return Latencies.Average();
        }
    }

    public ConcurrentBag<double> Latencies = new ConcurrentBag<double>();
    public ConcurrentBag<int> FailedRequests = new ConcurrentBag<int>();

    private int requestCount = 0;

    private long responseSize = 0;

    public int RequestCount
    {
        get
        {
            return requestCount;
        }
    }

    public long ResponseSize
    {
        get
        {
            return responseSize;
        }
    }


    public void Add(double latency, int responseLength)
    {
        Interlocked.Increment(ref requestCount);
        Interlocked.Add(ref responseSize, responseLength);
        Latencies.Add(latency);
    }
}


public class Options
{
    [Option('U', "url", Required = false, Default = "https://localhost:5000", HelpText = "Url to do load test against")]
    public string Url { get; set; }

    [Option('R', "run", Default = 3, HelpText = "Number of runs")]
    public int Runs { get; set; }

    [Option('D', "duration", Default = 20, HelpText = "Duration (seconds) to run the test")]
    public int Duration { get; set; }

    [Option('T', "thread", Default = 5, HelpText = "Count of threads")]
    public int Threads { get; set; }

    [Option('C', "connection", Default = 80, HelpText = "Concurrent connections per thread.")]
    public int Connections { get; set; }

    [Option('S', "streaming", Required = false, Default = false, HelpText = "whether to call the streaming rpc.")]
    public bool Streaming { get; set; }

    [Option("maxSize", Default = 1000000)]
    public int MaxSize { get; set; }

    [Option("minSize", Default = 10)]
    public int MinSize { get; set; }

    internal int Size { get; set; }
}


public class UnixDomainSocketsConnectionFactory
{
    private readonly EndPoint endPoint;

    public UnixDomainSocketsConnectionFactory(EndPoint endPoint)
    {
        this.endPoint = endPoint;
    }

    public async ValueTask<Stream> ConnectAsync(SocketsHttpConnectionContext _,
        CancellationToken cancellationToken = default)
    {
        var socket = new Socket(AddressFamily.Unix, SocketType.Stream, ProtocolType.Unspecified);

        try
        {
            await socket.ConnectAsync(this.endPoint, cancellationToken).ConfigureAwait(false);
            return new NetworkStream(socket, true);
        }
        catch
        {
            socket.Dispose();
            throw;
        }
    }
}

public class NamedPipesConnectionFactory
{
    private readonly string pipeName;

    public NamedPipesConnectionFactory(string pipeName)
    {
        this.pipeName = pipeName;
    }

    public async ValueTask<Stream> ConnectAsync(SocketsHttpConnectionContext _,
        CancellationToken cancellationToken = default)
    {
        var clientStream = new NamedPipeClientStream(
            serverName: ".",
            pipeName: this.pipeName,
            direction: PipeDirection.InOut,
            options: PipeOptions.WriteThrough | PipeOptions.Asynchronous,
            impersonationLevel: TokenImpersonationLevel.Anonymous);

        try
        {
            await clientStream.ConnectAsync(cancellationToken).ConfigureAwait(false);
            return clientStream;
        }
        catch
        {
            clientStream.Dispose();
            throw;
        }
    }
}
