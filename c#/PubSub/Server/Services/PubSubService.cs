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
using System.Threading;
using System.Threading.Tasks;
using Count;
using Google.Protobuf.WellKnownTypes;
using Grpc.Core;
using Microsoft.Extensions.Logging;

namespace Server.Services;

public class PubSubService : PubSub.PubSubBase
{
    private readonly ILogger _logger;
    private readonly MessageCenter messageCenter;

    public PubSubService(MessageCenter queue, ILoggerFactory loggerFactory)
    {
        messageCenter = queue;
        _logger = loggerFactory.CreateLogger<PubSubService>();
    }

    public override async Task Subscribe(Empty request, IServerStreamWriter<PublishReply> responseStream, ServerCallContext context)
    {
        // Use SemaphoreSlim instead of AutoResetEvent because it supports async wait
        SemaphoreSlim semaphore = new SemaphoreSlim(1, 1);

        // IMPORTANT: add the event before publishing the first message to avoid missing any update
        // between the time the first message is published and the event is added to the queue
        messageCenter.Queue.Enqueue(semaphore);

        bool isFirst = true;

        while (true)
        {
            // wait here
            await semaphore.WaitAsync();

            _logger.LogDebug("Publishing message to client");
            try
            {
                await responseStream.WriteAsync(new PublishReply
                {
                    Msg = messageCenter.Msg,
                    Ts = Timestamp.FromDateTime(DateTime.UtcNow)
                });

                if (isFirst)
                {
                    isFirst = false;
                    continue;
                }

                // listen again for the next event
                // Todo: there could be a chance that a subscriber was after this one might be inserted before this one
                // The result is the the other subscriber will get duplicate updates
                messageCenter.Queue.Enqueue(semaphore);
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "+++++Error writing to stream");
                break;
            }
        }
    }
}
