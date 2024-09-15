// This is a wrk like http benchmarking tool written in C# that supports http/3
using CommandLine;
using System.Collections.Concurrent;
using System.Diagnostics;
using System.Net;
using System.Net.Security;
using System.Runtime.InteropServices;
using System.Security.Cryptography.X509Certificates;

var latencies = new ConcurrentBag<double>();
var failedRequest = new ConcurrentBag<HttpStatusCode>();
int requestCount = 0;
long responseSize = 0;

// create a global client that will shared by all threads
var handler = new HttpClientHandler();
handler.ClientCertificateOptions = ClientCertificateOption.Manual;
handler.ServerCertificateCustomValidationCallback =
(HttpRequestMessage httpMessage, X509Certificate2 certificate2, X509Chain x509Chain, SslPolicyErrors sslPolicyErrors) =>
{
    return true; // Ignore the checks and return true
};

var client = new HttpClient(handler);
//var client = new HttpClient();

await Parser.Default.ParseArguments<Options>(args).WithParsedAsync(async o =>
{
    switch (o.HttpVersion)
    {
        case 0:
            // not specified, 1.1 by default
            // http/1.1 supports keep-alive but does not support multiplexing (true simultaneous concurrency on a single connection)
            // which means as many connections will be established as the number of concurrent requests
            break;
        case 1:
        case 2:
        case 3:
            client.DefaultRequestVersion = o.HttpVersion == 1 ? HttpVersion.Version11 : o.HttpVersion == 2 ? HttpVersion.Version20 : HttpVersion.Version30;
            client.DefaultVersionPolicy = HttpVersionPolicy.RequestVersionExact;

            break;
        default:
            throw new NotSupportedException("Invalid http version");
    }

    var tasks = new List<Task>();
    for (int i = 0; i < o.Threads; i++)
    {
        // Use Task.Run) to run the task in a new thread
        tasks.Add(Task.Run(() => RunThread(o)));
    }
    await Task.WhenAll(tasks);

    client.Dispose();

    // Print stats
    Console.WriteLine("Running {0}s test @ {1}", o.Duration, o.Url);
    Console.WriteLine("{0} threads and {1} connections", o.Threads, o.Connections);
    Console.WriteLine("\t{0} requests in {1}s, {2:F2}GB read", requestCount, o.Duration, 1.0 * responseSize / (1 << 30));
    if (failedRequest.Count > 0)
    {
        Console.WriteLine("Non-2xx or 3xx responses: {0}", failedRequest.Count);
    }
    Console.WriteLine("Requests/sec: {0}", requestCount / o.Duration);
    double avg = latencies.Average();
    Console.WriteLine("Average Latency: {0:F2}ms", avg);
});

async Task RunThread(Options o)
{
    // Console.WriteLine("[Thread] Thread id: " + Thread.CurrentThread.ManagedThreadId);
    var tasks = new List<Task>();

    for (int i = 0; i < (o.Connections / o.Threads); i++)
    {
        tasks.Add(RunConnection(client, o));
    }

    await Task.WhenAll(tasks);
}

async Task RunConnection(HttpClient client, Options o)
{
    // Console.WriteLine("[Connection] Thread id: " + Thread.CurrentThread.ManagedThreadId);

    var sw = Stopwatch.StartNew();
    double t;
    while (sw.Elapsed.TotalSeconds < o.Duration)
    {
        t = sw.Elapsed.TotalMilliseconds;
        HttpResponseMessage resp = await client.GetAsync(o.Url);
        string body = await resp.Content.ReadAsStringAsync();
        Interlocked.Increment(ref requestCount);
        Interlocked.Add(ref responseSize, body.Length);

        if (resp.StatusCode == HttpStatusCode.OK)
        {
            latencies.Add(sw.Elapsed.TotalMilliseconds - t);
        }
        else
        {
            failedRequest.Add(resp.StatusCode);
        }
    }
}

public class Options
{
    [Option('U', "url", Required = true, HelpText = "Url to do load test against")]
    public required string Url { get; set; }

    [Option('D', "duration", Required = true, HelpText = "Duration (seconds) to run the test")]
    public required uint Duration { get; set; }

    [Option('T', "thread", Required = true, HelpText = "Count of threads")]
    public required ushort Threads { get; set; }

    [Option('C', "connection", Required = true, HelpText = "Connections in total. Connections/Threads in each thread.")]
    public required ushort Connections { get; set; }

    [Option('H', "http", Required = false, HelpText = "Http version, allowed values are 1, 2, 3")]
    public required ushort HttpVersion { get; set; } = 0;
}