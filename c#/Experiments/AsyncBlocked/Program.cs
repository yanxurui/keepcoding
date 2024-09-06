using Microsoft.Identity.Client;

namespace ConsoleApp1
{
    using System.Diagnostics;
    using System.Threading;

    class Program
    {
        private static string GetTime()
        {
            return DateTime.Now.ToString("HH:mm:ss.fff");
        }

        private static async ValueTask<(int, int)> InternalProcess()
        {
            //lock (obj)
            //{
            //    Thread.Sleep(5000);
            //    return (1, 2);
            //}
            Console.WriteLine("  Before sleep");
            Thread.Sleep(5000);
            //await Task.Delay(5000);
            Console.WriteLine("  After sleep");

            return (1, 2);
        }

        private static async Task Process()
        {
            Console.WriteLine("  Before calling InternalProcess");
            var (a, b) = await InternalProcess();
            Console.WriteLine("  After calling InternalProcess");
        }

        static async Task Main(string[] args)
        {
            Console.WriteLine(GetTime());

            // This will block the main thread
            //var task = Process();

            // Long-term fix is to turn the synchronous code into asynchronous code.
            //     In this case, `Thread.Sleep(5000);` should be replaced by await Task.Delay(5000);
            // Short-term workaround: Use Task.Run to run the Process method in a background thread
            //var task = Task.Run(() => Process());
            var task = Task.Run(async () => await Process());

            Console.WriteLine(GetTime());

            await task;
            Console.WriteLine(GetTime());
        }
    }
}