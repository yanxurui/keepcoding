# MiniLidStack

A minimum-viable implementation of a "lidstack" — per-thread / per-async-context
structured diagnostic tracing in ~280 lines of pure C# with no custom buffer or
framing machinery.

## What's a lidstack?

A sequence of small records, each tagged with:

- a **LID** (Location ID) — a uint identifying the call site that emitted the record,
- a **layout** byte — what kind of record (Location, Dword, Guid, ...),
- an opaque payload of layout-specific bytes.

Trace methods append records as a request flows through code; at the end you
serialize for transport or stringify for logs. It's a structured, low-overhead
alternative to text-based logs for hot paths.

## Features

- **Per-thread or per-async-context storage** — `[ThreadStatic]` by default
  (auto-created), with `AsyncLocal` opt-in via `UseAsyncContext()` for code on
  shared ThreadPool threads.
- **5 record layouts**: `Location`, `Dword`, `DwordString`, `Guid`, `Version`.
- **Compact text format**: `"layout.lid:hex-payload, ..."` for log lines.
- **Binary wire format**: `[ushort version][int count][per record: layout, lid,
  ushort payload-length, payload bytes]`. Plain `BinaryWriter` over
  `MemoryStream`.

## Quick start

See `Program.cs` for runnable demos:

- **Demo 1** — single-process trace → serialize → deserialize-append round-trip.
- **Demo 2** — two-thread client/server splice: each thread keeps its own
  records, the "wire" is just a `byte[]` handed between them, and the client
  splices the server's records into its own stack between sentinel LIDs.

```
dotnet run
```

## Async caveat

On a multiplexed ThreadPool (gRPC, ASP.NET Core, Task.Run, ...), the
`[ThreadStatic]` fallback is silently wrong under concurrent requests sharing a
thread. Wrap each request boundary in:

```csharp
using (DiagnosticContext.UseAsyncContext())
{
    // your async handler here
}
```

The class-level XML doc in `DiagnosticContext.cs` walks through the exact
failure mode (the T1/T2 timeline) and discusses the always-AsyncLocal
alternative and its perf cost.

## Files

- `DiagnosticContext.cs` — the library (~280 lines).
- `Program.cs` — two runnable demos.
- `MiniLidStack.csproj` — net8.0 console app.
