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
using Server.Services;
using Microsoft.AspNetCore.Server.Kestrel.Core;
using Server;
using System.Threading;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.DependencyInjection;

// Default values on my laptop:
//   ProcessorCount: 12
//   Min worker threads: 12, I/O threads: 1
//   Max worker threads: 32767, I/O threads: 1000
int processorCount = Environment.ProcessorCount;
int minWorkerThreads = processorCount * 2; // Adjust as needed  
int minCompletionPortThreads = processorCount * 2; // Adjust as needed  
ThreadPool.SetMinThreads(minWorkerThreads, minCompletionPortThreads);

var builder = WebApplication.CreateBuilder(args);

builder.WebHost.ConfigureKestrel(serverOptions =>
{
    serverOptions.ListenAnyIP(5001, listenOptions =>
    {
        listenOptions.UseHttps();
        listenOptions.Protocols = HttpProtocols.Http2;
    });
});

builder.Services.AddGrpc();
builder.Services.AddSingleton<MessageCenter>();
builder.Services.AddHostedService<MyBackgroundService>();

var app = builder.Build();
app.MapGrpcService<CounterService>();

app.Run();
