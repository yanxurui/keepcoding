using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using System;
using System.Diagnostics;
using System.Threading;
using System.Threading.Tasks;

namespace Server.Services;

public class MyBackgroundService : BackgroundService
{
    private readonly ILogger _logger;

    private readonly MessageCenter messageCenter;

    public MyBackgroundService(MessageCenter mc, ILoggerFactory loggerFactory)
    {
        messageCenter = mc;
        _logger = loggerFactory.CreateLogger<MyBackgroundService>();
    }

    protected override async Task ExecuteAsync(CancellationToken stoppingToken)
    {
        while (!stoppingToken.IsCancellationRequested)
        {
            await Task.Delay(3000, stoppingToken);

            /****************Threads stats*********************/
            int workerThreads, completionPortThreads;
            ThreadPool.GetMinThreads(out workerThreads, out completionPortThreads);
            _logger.LogInformation($"Min worker threads: {workerThreads}, I/O threads: {completionPortThreads}");
            ThreadPool.GetMaxThreads(out workerThreads, out completionPortThreads);
            _logger.LogInformation($"Max worker threads: {workerThreads}, I/O threads: {completionPortThreads}");

            int availableWorker, availableAsyncIO;
            ThreadPool.GetAvailableThreads(out availableWorker, out availableAsyncIO);

            int maxWorkerThreads, maxCompletionPortThreads;
            ThreadPool.GetMaxThreads(out maxWorkerThreads, out maxCompletionPortThreads);

            int busyWorkerThreads = maxWorkerThreads - availableWorker;
            int busyAsyncIOThreads = maxCompletionPortThreads - availableAsyncIO;

            _logger.LogInformation("Worker Threads: " + busyWorkerThreads);
            _logger.LogInformation("Async I/O Threads: " + busyAsyncIOThreads);
            /*************************************/

            int count = messageCenter.Queue.Count;
            _logger.LogInformation($"MyBackgroundService is running. There are {count} subscribers.");
            messageCenter.Msg = $"The current time is: {DateTime.Now}";

            // iterate all events in the queue and send them to all clients
            // measure time elapsed
            Stopwatch sw = new();
            sw.Start();

            for (int i = 0; i < count; i++)
            {
                if (messageCenter.Queue.TryDequeue(out var e))
                {
                    // signal the event to wake up the corresponding listener
                    e.Set();
                }
                else
                {
                    // we should never reach here because there is only one thread that dequeues events
                    _logger.LogError("Failed to dequeue an event");
                }
            }

            sw.Stop();
            _logger.LogInformation($"Time elapsed: {sw.ElapsedMilliseconds} ms");
        }
    }
}
