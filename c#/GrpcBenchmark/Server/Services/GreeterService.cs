using Google.Protobuf;
using Google.Protobuf.WellKnownTypes;
using Grpc.Core;
using Greet;
using System.Diagnostics;

namespace GrpcGreeter.Services;

public class GreeterService : Greeter.GreeterBase
{
    private static Dictionary<uint, ByteString> responseMap;

    static GreeterService()
    {
        responseMap = new Dictionary<uint, ByteString>();
        for (uint size = 10; size <= 1000000; size *= 10)
        {
            responseMap.Add(size, ByteString.CopyFrom(new byte[size]));
        }
    }


    private readonly ILogger<GreeterService> _logger;
    public GreeterService(ILogger<GreeterService> logger)
    {
        _logger = logger;
    }

    private static ByteString GetByteString(uint size)
    {
        if (!responseMap.TryGetValue(size, out ByteString? byteString))
        {
            if (size > 1000000000)
            {
                // 1 KB by default
                byteString = responseMap[1000];
            }
            else
            {
                byteString = ByteString.CopyFrom(new byte[size]);
                responseMap.Add(size, byteString);
            }
        }

        return byteString;
    }

    public override Task<HelloReply> SayHello(HelloRequest request, ServerCallContext context)
    {
        return Task.FromResult(new HelloReply
        {
            Message = "Hello " + request.Name
        });
    }

    public override Task<DownloadReply> Download(DownloadRequest request, ServerCallContext context)
    {
        ByteString byteString = GetByteString(request.RequestSize);

        return Task.FromResult(new DownloadReply
        {
            Body = byteString
        });
    }

    public override async Task DownloadStream(IAsyncStreamReader<DownloadRequest> requestStream, IServerStreamWriter<DownloadReply> responseStream, ServerCallContext context)
    {
        while (await requestStream.MoveNext() && !context.CancellationToken.IsCancellationRequested)
        {
            uint requestSize = requestStream.Current.RequestSize;
            ByteString byteString = GetByteString(requestSize);

            await responseStream.WriteAsync(new DownloadReply
            {
                Body = byteString
            });
        }
    }

    public override Task<Empty> Sleep(SleepRequest request, ServerCallContext context)
    {
        // use sleep to mimic blocking operation
        Thread.Sleep((int)(1000 * request.Seconds));
        int threadId = Thread.CurrentThread.ManagedThreadId;
        _logger.LogInformation($"Thread id: {threadId}");
        return Task.FromResult(new Empty());
    }
}
