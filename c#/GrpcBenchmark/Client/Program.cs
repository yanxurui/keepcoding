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
        // print in csv format for easy copy-paste to spreadsheet
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
        // Use Task.Run to run the task in a seperate thread
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
            currentCount = result.RequestCount;
            pbar.Tick($"Payload: {o.Size}, QPS: {currentCount-lastCount} reqs/sec");
            lastCount = currentCount;
        }
    }

    // Print stats
    Console.WriteLine("{0} requests in {1}s, {2:F2}GB read", result.RequestCount, result.Duration, 1.0 * result.ResponseSize / (1 << 30));
    if (result.FailedRequestCount > 0)
    {
        Console.WriteLine("Errored responses: {0}", result.FailedRequestCount);
    }
    Console.WriteLine("Requests/sec: {0}", result.RequestPerSecond);
    Console.WriteLine("Average Latency: {0:F2}ms", result.AverageLatency);
    Console.WriteLine("P95 Latency: {0:F2}ms", result.GetPercentileLatency(0.95));
    Console.WriteLine("P99 Latency: {0:F2}ms", result.GetPercentileLatency(0.99));
    Console.WriteLine("Top 5 Latencies:");
    foreach (var latency in result.GetTopLatenies(5))
    {
        Console.WriteLine("{0:F2}", latency);
    }

    return result;
}

async Task RunThread(Options o, Result result)
{
    var tasks = new List<Task>();
    var channel = CreateChannel(o.Url);
    var client = new Greeter.GreeterClient(channel);
    for (int i = 0; i < o.Connections; i++)
    {
        if (o.Streaming)
        {
            tasks.Add(RunConnectionStreaming(client, o, result));
        }
        else
        {
            tasks.Add(RunConnection(client, o, result));
        }
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

        try
        {
            reply = await client.DownloadAsync(downloadRequest);
        }
        catch (RpcException ex)
        {
            // Handle gRPC-specific exceptions
            Console.WriteLine($"gRPC error: {ex.Status.Detail}");
            reply = null;
        }

        // await channel.ShutdownAsync();

        result.Add(sw.Elapsed.TotalMilliseconds - t, reply == null? 0: reply.Body.Length, reply == null);
    }
}

async Task RunConnectionStreaming(Greeter.GreeterClient client, Options o, Result result)
{
    double t;
    DownloadRequest downloadRequest = new DownloadRequest { RequestSize = (uint)o.Size };
    using var stream = client.DownloadStream();
    DownloadReply reply;

    var sw = Stopwatch.StartNew();

    while (sw.Elapsed.TotalSeconds < o.Duration)
    {
        t = sw.Elapsed.TotalMilliseconds;

        try
        {
            await stream.RequestStream.WriteAsync(downloadRequest);

            // Receive the response. Is this the right way to use streaming?
            if (await stream.ResponseStream.MoveNext(CancellationToken.None))
            {
                reply = stream.ResponseStream.Current;
            }
            else
            {
                Console.WriteLine("streaming has completed unexpectedly");
                break;
            }
        }
        catch (RpcException ex)
        {
            // Handle gRPC-specific exceptions
            Console.WriteLine($"gRPC error: {ex.Status.Detail}");
            reply = null;
        }

        result.Add(sw.Elapsed.TotalMilliseconds - t, reply == null? 0 : reply.Body.Length, reply == null);
    }

    await stream.RequestStream.CompleteAsync();

    // Receive remaining responses from the server  
    while (await stream.ResponseStream.MoveNext(CancellationToken.None))
    {
        reply = stream.ResponseStream.Current;
        throw new Exception("Unexpected response from server");
    }
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
    private long responseSize = 0;

    public double Duration { get; set; }

    private ConcurrentBag<double> latencies = new ConcurrentBag<double>();

    private int failedRequestCount = 0;

    private IList<double> latenciesOrdered = null;

    public int RequestCount
    {
        get
        {
            return latencies.Count;
        }
    }

    public int FailedRequestCount
    {
        get
        {
            return failedRequestCount;
        }
    }

    public long ResponseSize
    {
        get
        {
            return responseSize;
        }
    }

    public int RequestPerSecond
    {
        get
        {
            return (int)(RequestCount / Duration);
        }
    }

    public double AverageLatency
    {
        get
        {
            if (latencies.Count == 0)
            {
                return 0;
            }

            return latencies.Average();
        }
    }

    public IList<double> LatenciesOrdered
    {
        get
        {
            if (latenciesOrdered == null)
            {
                latenciesOrdered = latencies.OrderBy(latency => latency).ToList();
            }

            return latenciesOrdered;
        }

    }

    public void Add(double latency, int responseLength, bool failed = false)
    {
        Interlocked.Add(ref responseSize, responseLength);
        latencies.Add(latency);

        if (failed)
        {
            Interlocked.Increment(ref failedRequestCount);
        }
    }

    
    public double GetPercentileLatency(double percentile)
    {
        if (LatenciesOrdered.Count == 0)
        {
            return 0;
        }

        int index = (int)(percentile * LatenciesOrdered.Count);
        return LatenciesOrdered[index];
    }

    public List<double> GetTopLatenies(int count)
    {
        return LatenciesOrdered.TakeLast(count).ToList();
    }
}


public class Options
{
    [Option('U', "url", Required = false, Default = "https://localhost:5001", HelpText = "Url to do load test against")]
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
