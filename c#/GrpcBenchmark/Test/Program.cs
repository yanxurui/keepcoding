using System.Diagnostics;
using System.Threading.Tasks;
using Google.Protobuf.WellKnownTypes;
using Grpc.Core;
using Grpc.Net.Client;
using Greet;
using System.Threading.Channels;

// The port number must match the port of the gRPC server.
var url = "https://localhost:5001";
//using var channel = GrpcChannel.ForAddress(url);
//var client = new Greeter.GreeterClient(channel);
DownloadRequest downloadRequest = new DownloadRequest { RequestSize = 10 };

// TestTimeout();

SocketsHttpHandler socketsHttpHandler = new() { EnableMultipleHttp2Connections = true };

GrpcChannelOptions channelOptions = new()
{
    DisposeHttpClient = true
};

channelOptions.HttpClient = new HttpClient(socketsHttpHandler);

using var channel = GrpcChannel.ForAddress(url, channelOptions);
var client = new Greeter.GreeterClient(channel);

var stream = client.DownloadStream();

foreach (var i in Enumerable.Range(0, 2))
{

    await stream.RequestStream.WriteAsync(downloadRequest);

    await stream.ResponseStream.MoveNext();
}

await stream.RequestStream.CompleteAsync();


void TestTimeout()
{
    SocketsHttpHandler socketsHttpHandler = new() { EnableMultipleHttp2Connections = true };

    GrpcChannelOptions channelOptions = new()
    {
        DisposeHttpClient = true
    };

    channelOptions.HttpClient = new HttpClient(socketsHttpHandler);

    var channel = GrpcChannel.ForAddress(url, channelOptions);
    var client = new Greeter.GreeterClient(channel);
    client.Sleep(new SleepRequest { Seconds = 105 });
    Console.WriteLine("Done");
}

/// <summary>
/// Test blocking operations in the server side will create new threads
/// </summary>
async Task Sleep()
{
    Task<Empty> sleep5 = client.SleepAsync(new SleepRequest { Seconds = 5 }).ResponseAsync;
    Task<Empty> sleep1 = client.SleepAsync(new SleepRequest { Seconds = 0 }).ResponseAsync;
    Task task1 = Sleep(5);
    Task task2 = Sleep(1);
    await PrintThread();

    async Task Sleep(int seconds)
    {
        await client.SleepAsync(new SleepRequest { Seconds = (uint)seconds });
        await PrintThread();
    }
}

/// <summary>
/// Test if concurrent requests in the client can share the same thread
/// </summary>
async Task ConcurrentDownload()
{
    Stopwatch stopwatch = new Stopwatch();
    stopwatch.Start();

    List<Task> tasks = new List<Task>();
    for (int i = 0; i < 10; i++)
    {
        tasks.Add(DownloadStream());
    }
    await Task.WhenAll(tasks);

    stopwatch.Stop();
    Console.WriteLine("Elapsed time {0} seconds", stopwatch.Elapsed.TotalSeconds);
}


/// <summary>
/// Verify that EnableKernelResponseBuffering can help to improve throughput for large responses.
/// 2 vs 14 seconds
/// </summary>
async Task LargeResponse()
{
    // http.sys
    using var channel = GrpcChannel.ForAddress(
        "https://127.0.0.1:5002",
        new GrpcChannelOptions
        {
            MaxReceiveMessageSize = 200 * 1024 * 1024
        });

    Stopwatch stopwatch = new Stopwatch();
    stopwatch.Start();

    var resp = await client.DownloadAsync(new DownloadRequest { RequestSize = 200_000_000 });
    File.WriteAllBytes(@".\out", resp.Body.ToByteArray());

    stopwatch.Stop();
    Console.WriteLine("Elapsed time {0} seconds", stopwatch.Elapsed.TotalSeconds);
}

async Task DownloadStream()
{
    var stream = client.DownloadStream();

    for (int i = 0; i < 1; i++)
    {
        await stream.RequestStream.WriteAsync(downloadRequest);
    }

    await stream.RequestStream.CompleteAsync();

    while (await stream.ResponseStream.MoveNext())
    {
        DownloadReply reply = stream.ResponseStream.Current;
        await PrintThread();
    }
}
async Task PrintThread()
{
    int threadId = Thread.CurrentThread.ManagedThreadId;
    Console.WriteLine($"Thread id: {threadId}");
}

async Task TestIsCompleted()
{
    // create an array of 3 tasks with each of them waiting for 1, 2, 3 seconds
    Task[] tasks = new Task[3];
    for (int i = 0; i < 3; i++)
    {
        int seconds = i + 1;
        tasks[i] = Task.Run(async () =>
        {
            await Task.Delay(seconds * 1000);
        });
    }

    Task waitingTask = Task.WhenAll(tasks);

    // check if the task is completed every 1 second
    while (!waitingTask.IsCompleted)
    {
        Console.WriteLine("still running");
        await Task.Delay(1000);
    }
}