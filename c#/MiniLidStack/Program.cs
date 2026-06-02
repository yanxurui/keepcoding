// Runnable demos for the minimum lidstack implementation:
//   Demo 1 — single-process trace, serialize, deserialize-append.
//   Demo 2 — cross-thread splice: client thread + server thread, each with its own
//            per-thread context (auto-created on first Trace), communicating via a
//            serialized byte[] (the "wire").

using MiniLidStack;

Console.WriteLine("=== Demo 1: single-process trace → wire → restore ===");
Demo1();

Console.WriteLine();
Console.WriteLine("=== Demo 2: cross-thread splice (client thread + server thread) ===");
Demo2();

static void Demo1()
{
    DiagnosticContext.Reset();

    DiagnosticContext.TraceDwordString(new LID(55847), 240, "EcDoRpc");
    DiagnosticContext.TraceVersion(new LID(52176), new Version(15, 20, 1856, 0));
    DiagnosticContext.TraceGuid(new LID(45434), Guid.Parse("cda86662-7cb9-436e-96b9-9e79c8b065dd"));

    string compact = DiagnosticContext.ToCompactString();
    Console.WriteLine($"Compact: {compact}");

    byte[] wire = DiagnosticContext.Serialize();
    Console.WriteLine($"Wire ({wire.Length} bytes): {Convert.ToHexString(wire)}");

    // Simulate "transfer": reset (fresh process), then deserialize-append.
    DiagnosticContext.Reset();
    DiagnosticContext.AppendFromBytes(wire);

    Console.WriteLine($"After restore: {DiagnosticContext.ToCompactString()}");
}

static void Demo2()
{
    // The "wire" between client and server — just a byte[] handed off between threads.
    // In a real system this would be an RPC payload / TCP frame / etc.
    byte[]? serverWire = null;

    Thread clientThread = new(() =>
    {
        // The client thread's first Trace call auto-creates its own [ThreadStatic] list.
        DiagnosticContext.TraceDwordString(new LID(55847), 240, "EcDoRpc called");

        Console.WriteLine($"[client tid={Environment.CurrentManagedThreadId}] before RPC: {DiagnosticContext.ToCompactString()}");

        // Spawn the server thread and wait for its response.
        Thread serverThread = new(() =>
        {
            // Brand-new thread → brand-new [ThreadStatic] list. The client's records are
            // NOT visible here — that's the whole point of thread isolation.
            DiagnosticContext.TraceVersion(new LID(50032), new Version(15, 20, 1856, 6000));
            DiagnosticContext.TraceLocation(new LID(23226));                // --- ROP Parse Start ---
            DiagnosticContext.TraceDword(new LID(27962), 3);                // ROP: ropOpenMessage
            DiagnosticContext.TraceGuid(new LID(45434), Guid.Parse("cda86662-7cb9-436e-96b9-9e79c8b065dd"));
            DiagnosticContext.TraceLocation(new LID(31418));                // --- ROP Parse Done ---

            Console.WriteLine($"[server tid={Environment.CurrentManagedThreadId}] stack:      {DiagnosticContext.ToCompactString()}");

            // Ship the server stack back to the client by serializing into the shared byte[].
            serverWire = DiagnosticContext.Serialize();
        });

        serverThread.Start();
        serverThread.Join();

        // Back on the client thread — its records are still intact, the server thread didn't touch them.
        DiagnosticContext.TraceLocation(new LID(1494));         // ---- Remote Context Beg ----
        DiagnosticContext.AppendFromBytes(serverWire!);         // splice the server records in
        DiagnosticContext.TraceLocation(new LID(1750));         // ---- Remote Context End ----

        DiagnosticContext.TraceDword(new LID(43559), 0);        // EcDoRpc returned

        Console.WriteLine($"[client tid={Environment.CurrentManagedThreadId}] merged:     {DiagnosticContext.ToCompactString()}");
    });

    clientThread.Start();
    clientThread.Join();
}
