local ffi=require"ffi"

-- https://stackoverflow.com/questions/9073667/where-to-find-the-complete-definition-of-off-t-type
-- gcc -E a.c|grep ssize_t
ffi.cdef[[
typedef long int off_t;
typedef long int ssize_t;
int fileno(struct FILE* stream);
ssize_t pread(int fd, void *buf, size_t count, off_t offset);
]]

local function pread(file, count, offset)
    local fd = ffi.C.fileno(file)
    -- allocates a byte buffer of this size
    local buf = ffi.new("uint8_t[?]", count)
    ffi.C.pread(fd, buf, count, offset)
    -- copy to a lua string
    -- how to avoid copying?
    return ffi.string(buf, count)
end


-- test

-- cat temp
-- 12helloworld
local f=io.open('temp', 'r')

local offset = 2
local count = 5
print(pread(f, count, offset))
