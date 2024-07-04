#region Copyright notice and license

// Copyright 2019 The gRPC Authors
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#endregion

using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Net.Http;
using System.Threading.Tasks;
using Count;
using Google.Protobuf.WellKnownTypes;
using Grpc.Core;
using Grpc.Net.Client;

using var channel = GrpcChannel.ForAddress("https://localhost:5001", new GrpcChannelOptions
{
    HttpHandler = new SocketsHttpHandler
    {
        EnableMultipleHttp2Connections = true,

        // ...configure other handler settings
    }
});

int numberOfSubscribers = 10;
if (args.Count() > 0)
{
    // parse the first argument to get the number of subscribers
    numberOfSubscribers = int.Parse(args[0]);
}

var tasks = new List<Task>();
Random rand = new Random();
for (int i = 1; i <= numberOfSubscribers; i++)
{
    // add some random delay to simulate the different time to connect to the server
    int delayed = rand.Next(0, numberOfSubscribers * 30);
    tasks.Add(ServerStreamingCallExample(channel, i, delayed));
}
await Task.WhenAll(tasks);

static async Task ServerStreamingCallExample(GrpcChannel channel, int i, int delayed)
{
    await Task.Delay(delayed);
    Console.WriteLine($"{i}: connecting to the server with delay {delayed} ms");
    Stopwatch sw = new();
    sw.Start();
    bool fired = false;
    var client = new Counter.CounterClient(channel);
    using var call = client.Subscribe(new Empty());
    try
    {
        await foreach (var message in call.ResponseStream.ReadAllAsync())
        {
            if (!fired)
            {
                sw.Stop();
                fired = true;
                Console.WriteLine($"{i}: Connected and received the first message after {sw.ElapsedMilliseconds} ms");
            }

            Console.WriteLine($"{i}: {message.Msg}");
        }
    }
    catch (RpcException ex)
    {
        Console.WriteLine($"{i}: +++++Error reading response {ex}");
    }
}
