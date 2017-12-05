function low ()
    mid()
end

function mid()
    high(5)
end

function high(val)
    print (val)
end


local debugInfo = { caller = nil, callee = nil }
function hook()
    local info = debug.getinfo(2)
    if info == nil then
        debugInfo.callee = nil
        return
    end

    -- we only want to watch lua function calls (not C functions)
    if info.what ~= "Lua" then
        debugInfo.callee = "C function"
        return
    end

    debugInfo.caller = debugInfo.callee
    debugInfo.callee = info.name
    
    if debugInfo.caller ~= nil and debugInfo.callee ~= nil then
        msg = debugInfo.callee.. " was called by ".. debugInfo.caller.. "!"
        print(msg)
    end
end


debug.sethook(hook, "c")
low()
debug.sethook()
