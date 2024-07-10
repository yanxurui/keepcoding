using System.Diagnostics;
using System.Threading.Tasks;
using Google.Protobuf.WellKnownTypes;
using Grpc.Core;
using Grpc.Net.Client;
using Greet;

// The port number must match the port of the gRPC server.
using var channel = GrpcChannel.ForAddress("https://localhost:5001");
var client = new Greeter.GreeterClient(channel);
DownloadRequest downloadRequest = new DownloadRequest { RequestSize = 10 };

Stopwatch stopwatch = new Stopwatch();
stopwatch.Start();

//Task<Empty> sleep5 = client.SleepAsync(new SleepRequest { Seconds = 0 }).ResponseAsync;
//Task<Empty> sleep1 = client.SleepAsync(new SleepRequest { Seconds = 0 }).ResponseAsync;
//Task task1 = Sleep(5);
//Task task2 = Sleep(1);
//Task task1 = DownloadStream();
//Task task2 = DownloadStream();
//await PrintThread();
List<Task> tasks = new List<Task>();
for (int i = 0; i < 10; i++)
{
    tasks.Add(DownloadStream());
}
await Task.WhenAll(tasks);

stopwatch.Stop();
Console.WriteLine("Elapsed time {0} seconds", stopwatch.Elapsed.TotalSeconds);

async Task Sleep(int seconds)
{
    await client.SleepAsync(new SleepRequest { Seconds = (uint)seconds });
    int threadId = Thread.CurrentThread.ManagedThreadId;
    Console.WriteLine($"Thread id: {threadId}");
    //await PrintThread();
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
        // Process each reply here
        await PrintThread();
    }
}

async Task PrintThread()
{
    int threadId = Thread.CurrentThread.ManagedThreadId;
    Console.WriteLine($"Thread id: {threadId}");
}
