// Minimum lidstack implementation, modeled after Substrate's
// Microsoft.Exchange.Diagnostics.DiagnosticContext but stripped to the essentials:
//
//   - Backing storage: per-thread by default ([ThreadStatic]) with an optional
//     per-async-context override (AsyncLocal). Both auto-create on first access.
//   - Five record layouts: Location, Dword, DwordString, Guid, Version.
//   - Compact text format ("layout.lid:payload, ...") for logging.
//   - Binary wire format for serialization + cross-process / cross-thread splicing.

namespace MiniLidStack;

using System.Buffers.Binary;
using System.Text;

/// <summary>
/// Location ID — the unique trace call site identifier. Just a uint under the hood.
/// </summary>
public readonly record struct LID(uint Value)
{
    public override string ToString() => this.Value.ToString();
}

/// <summary>
/// Record layout identifier. Numeric values mirror Substrate's layout numbering so
/// the compact format is interchangeable.
/// </summary>
public enum Layout : byte
{
    Location = 0,
    Dword = 1,
    DwordString = 5,
    Guid = 8,
    Version = 20,
}

/// <summary>
/// A single diagnostic record: layout id, LID, and an opaque payload.
/// </summary>
public sealed record Record(Layout Layout, uint Lid, byte[] Payload);

/// <summary>
/// Per-thread (or per-async-context) diagnostic context. All Trace methods append to
/// a thread/async-local list; callers serialize/dump at end of request and Reset on
/// next request.
///
/// Storage: AsyncLocal (opt-in via UseAsyncContext) wins when set, otherwise
/// [ThreadStatic] auto-creates on first access. Same model as Substrate's
/// DiagnosticContext: cheap sync default, AsyncLocal opt-in for async code.
///
/// Footgun: if async code forgets UseAsyncContext on a shared ThreadPool, the
/// ThreadStatic fallback is silently wrong under concurrency:
///
///   Time   Thread T1                          Thread T2
///   ----   ---------------------------------  --------------------------
///   t0     Request A: Reset()                 (idle)
///   t1     Request A: TraceDword(X)
///   t2     Request A: await SomeIo()          (A's continuation queued)
///   t3     Request B: Reset()  ← wipes X too!
///   t4     Request B: TraceDword(Z)           Request A resumes here
///   t5                                        Request A: TraceDword(Y)
///                                             → adds to T2's fresh list
///                                             → A ends up with just [Y]
///                                             → X is gone, B has [Z]
///
/// No exception, no warning — just diagnostic data that's wrong in ways that
/// are hard to spot until oncall needs it.
///
/// Alternative: drop ThreadStatic and always auto-create into AsyncLocal.
/// Removes the footgun, but every Trace pays AsyncLocal's ~10× access cost
/// (low tens of ns) plus an ExecutionContext CoW on the first write per
/// request. Right trade for overwhelmingly-async servers; wrong for hot
/// sync paths. We keep ThreadStatic as default — know which side you're on.
/// </summary>
public static class DiagnosticContext
{
    /// <summary>Per-async-context override. Null = fall through to thread-local.</summary>
    private static readonly AsyncLocal<List<Record>?> asyncLocal = new();

    /// <summary>Per-thread fallback. Auto-created lazily.</summary>
    [ThreadStatic]
    private static List<Record>? threadLocal;

    /// <summary>
    /// Returns the active record list, creating it lazily if needed.
    /// Prefers AsyncLocal (when an async scope is active), falls back to ThreadStatic.
    /// </summary>
    private static List<Record> Records
    {
        get
        {
            List<Record>? list = asyncLocal.Value;
            if (list != null)
            {
                return list;
            }

            list = threadLocal;
            if (list == null)
            {
                list = new List<Record>();
                threadLocal = list;
            }

            return list;
        }
    }

    /// <summary>Wipe the active record list (call at start of each request).</summary>
    public static void Reset() => Records.Clear();

    /// <summary>Read-only snapshot of the active records.</summary>
    public static IReadOnlyList<Record> Snapshot() => Records.ToArray();

    /// <summary>
    /// Start a fresh per-async-context lidstack for the duration of the returned scope.
    /// REQUIRED at the start of any request handler that runs on shared threads
    /// (gRPC handler, ASP.NET Core endpoint, Task.Run continuation, any ThreadPool-
    /// backed async work). Without it, the implementation falls back to ThreadStatic,
    /// which silently corrupts records under concurrent requests sharing the same
    /// OS thread. See the class-level doc for the full failure mode.
    /// </summary>
    public static IDisposable UseAsyncContext()
    {
        List<Record>? previous = asyncLocal.Value;
        asyncLocal.Value = new List<Record>();
        return new AsyncContextScope(previous);
    }

    private sealed class AsyncContextScope : IDisposable
    {
        private readonly List<Record>? previous;

        public AsyncContextScope(List<Record>? previous)
        {
            this.previous = previous;
        }

        public void Dispose()
        {
            asyncLocal.Value = this.previous;
        }
    }

    // -------- Trace methods --------

    public static void TraceLocation(LID lid)
    {
        Records.Add(new Record(Layout.Location, lid.Value, Array.Empty<byte>()));
    }

    public static void TraceDword(LID lid, uint info)
    {
        byte[] payload = new byte[4];
        BinaryPrimitives.WriteUInt32LittleEndian(payload, info);
        Records.Add(new Record(Layout.Dword, lid.Value, payload));
    }

    public static void TraceGuid(LID lid, Guid guid)
    {
        Records.Add(new Record(Layout.Guid, lid.Value, guid.ToByteArray()));
    }

    public static void TraceDwordString(LID lid, uint info, string str)
    {
        byte[] strBytes = Encoding.ASCII.GetBytes(str);
        byte[] payload = new byte[4 + strBytes.Length];
        BinaryPrimitives.WriteUInt32LittleEndian(payload.AsSpan(0), info);
        strBytes.CopyTo(payload, 4);
        Records.Add(new Record(Layout.DwordString, lid.Value, payload));
    }

    public static void TraceVersion(LID lid, Version version)
    {
        byte[] payload = new byte[8];
        BinaryPrimitives.WriteUInt16LittleEndian(payload.AsSpan(0), (ushort)version.Major);
        BinaryPrimitives.WriteUInt16LittleEndian(payload.AsSpan(2), (ushort)version.Minor);
        BinaryPrimitives.WriteUInt16LittleEndian(payload.AsSpan(4), (ushort)version.Build);
        BinaryPrimitives.WriteUInt16LittleEndian(payload.AsSpan(6), (ushort)version.Revision);
        Records.Add(new Record(Layout.Version, lid.Value, payload));
    }

    // -------- Compact text format ("layout.lid:hex-payload, ...") --------

    /// <summary>
    /// Emit the active stack as "{layout}.{lid}:{hex}" entries joined by ", ".
    /// Same shape findlid's CompactLidStackParser reads.
    /// </summary>
    public static string ToCompactString() => FormatCompact(Records);

    /// <summary>Static formatter — also reusable for an externally provided record list.</summary>
    public static string FormatCompact(IEnumerable<Record> records)
    {
        StringBuilder sb = new();
        bool first = true;
        foreach (Record r in records)
        {
            if (!first)
            {
                sb.Append(", ");
            }

            first = false;
            sb.Append((byte)r.Layout);
            sb.Append('.');
            sb.Append(r.Lid);
            if (r.Payload.Length > 0)
            {
                sb.Append(':');
                sb.Append(Convert.ToHexString(r.Payload));
            }
        }

        return sb.ToString();
    }

    // -------- Wire format (for cross-process / cross-thread transfer) --------
    //
    //   ushort  version (always 0)
    //   int     record count
    //   per record:
    //     byte    layout
    //     uint    lid
    //     ushort  payload length
    //     bytes   payload
    //

    /// <summary>Serialize the active stack to a byte[] for transport.</summary>
    public static byte[] Serialize() => SerializeRecords(Records);

    /// <summary>Serialize an arbitrary record list to the same wire format.</summary>
    public static byte[] SerializeRecords(IReadOnlyList<Record> source)
    {
        using MemoryStream ms = new();
        using BinaryWriter bw = new(ms);
        bw.Write((ushort)0);
        bw.Write(source.Count);
        foreach (Record r in source)
        {
            bw.Write((byte)r.Layout);
            bw.Write(r.Lid);
            bw.Write((ushort)r.Payload.Length);
            bw.Write(r.Payload);
        }

        return ms.ToArray();
    }

    /// <summary>
    /// Deserialize a wire-format blob and append its records to the active stack.
    /// Use this on the client side after receiving the server's stack to splice the
    /// two together.
    /// </summary>
    public static void AppendFromBytes(byte[] data)
    {
        foreach (Record r in DeserializeRecords(data))
        {
            Records.Add(r);
        }
    }

    /// <summary>Parse a wire-format blob into a list of records (no thread-local side effect).</summary>
    public static List<Record> DeserializeRecords(byte[] data)
    {
        using MemoryStream ms = new(data);
        using BinaryReader br = new(ms);
        ushort version = br.ReadUInt16();
        if (version != 0)
        {
            throw new InvalidDataException($"Unknown wire version {version}");
        }

        int count = br.ReadInt32();
        List<Record> result = new(count);
        for (int i = 0; i < count; i++)
        {
            Layout layout = (Layout)br.ReadByte();
            uint lid = br.ReadUInt32();
            ushort payloadLen = br.ReadUInt16();
            byte[] payload = br.ReadBytes(payloadLen);
            result.Add(new Record(layout, lid, payload));
        }

        return result;
    }
}
