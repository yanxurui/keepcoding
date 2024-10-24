using Microsoft.VisualStudio.TestTools.UnitTesting;
using System.Diagnostics;
using System.Threading.Tasks;
using Google.Protobuf.WellKnownTypes;
using Grpc.Core;
using Grpc.Net.Client;
using Greet;
using System.Threading.Channels;
using System.Net.Http;
using System.Collections.Generic;
using System.Linq;
using System.IO;
using System;

namespace Test
{
    [TestClass]
    public class Test
    {
        private readonly string url = "https://localhost:5001";
        private Greeter.GreeterClient client;
        private DownloadRequest downloadRequest;

        [TestInitialize]
        public void Initialize()
        {
            var channel = GrpcChannel.ForAddress(url);
            client = new Greeter.GreeterClient(channel);
            downloadRequest = new DownloadRequest { RequestSize = 10 };
        }

        [TestMethod]
        public async Task TestClient()
        {
            SocketsHttpHandler socketsHttpHandler = new() { EnableMultipleHttp2Connections = true };

            GrpcChannelOptions channelOptions = new()
            {
                DisposeHttpClient = true,
                HttpClient = new HttpClient(socketsHttpHandler)
            };

            using var channel = GrpcChannel.ForAddress(url, channelOptions);
            var client = new Greeter.GreeterClient(channel);

            var stream = client.DownloadStream();

            foreach (var i in Enumerable.Range(0, 2))
            {
                await stream.RequestStream.WriteAsync(downloadRequest);
                await stream.ResponseStream.MoveNext();
            }

            await stream.RequestStream.CompleteAsync();
        }

        [TestMethod]
        public void TestTimeout()
        {
            SocketsHttpHandler socketsHttpHandler = new() { EnableMultipleHttp2Connections = true };

            GrpcChannelOptions channelOptions = new()
            {
                DisposeHttpClient = true,
                HttpClient = new HttpClient(socketsHttpHandler)
            };

            var channel = GrpcChannel.ForAddress(url, channelOptions);
            var client = new Greeter.GreeterClient(channel);
            client.Sleep(new SleepRequest { Seconds = 105 });
            Console.WriteLine("Done");
        }

        [TestMethod]
        public async Task Sleep()
        {
            Task<Empty> sleep5 = client.SleepAsync(new SleepRequest { Seconds = 5 }).ResponseAsync;
            Task<Empty> sleep0 = client.SleepAsync(new SleepRequest { Seconds = 0 }).ResponseAsync;
            Task task1 = Sleep(5);
            Task task2 = Sleep(1);
            PrintThread();

            async Task Sleep(int seconds)
            {
                await client.SleepAsync(new SleepRequest { Seconds = (uint)seconds });
                PrintThread();
            }

            await Task.WhenAll(sleep5, sleep0, task1, task2);
        }

        [TestMethod]
        public async Task ConcurrentDownload()
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

        [TestMethod]
        public async Task LargeResponse()
        {
            using var channel = GrpcChannel.ForAddress(
                "https://127.0.0.1:5002",
                new GrpcChannelOptions
                {
                    MaxReceiveMessageSize = 200 * 1024 * 1024
                });

            var client = new Greeter.GreeterClient(channel);

            Stopwatch stopwatch = new Stopwatch();
            stopwatch.Start();

            var resp = await client.DownloadAsync(new DownloadRequest { RequestSize = 200_000_000 });
            File.WriteAllBytes(@".\out", resp.Body.ToByteArray());

            stopwatch.Stop();
            Console.WriteLine("Elapsed time {0} seconds", stopwatch.Elapsed.TotalSeconds);
        }

        [TestMethod]
        public async Task DownloadStream()
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
                PrintThread();
            }
        }

        [TestMethod]
        public async Task TestIsCompleted()
        {
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

            while (!waitingTask.IsCompleted)
            {
                Console.WriteLine("still running");
                await Task.Delay(1000);
            }
        }

        private void PrintThread()
        {
            int threadId = Thread.CurrentThread.ManagedThreadId;
            Console.WriteLine($"Thread id: {threadId}");
        }
    }
}