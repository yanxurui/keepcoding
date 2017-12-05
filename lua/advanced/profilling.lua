local calls, total, this = {}, {}, {}
debug.sethook(function(event)
  local i = debug.getinfo(2, "Sln")
  if i.what ~= 'Lua' then return end
  local func = i.name or (i.source..':'..i.linedefined)
  if event == 'call' then
    this[func] = os.clock()
  else
    local time = os.clock() - this[func]
    total[func] = (total[func] or 0) + time
    calls[func] = (calls[func] or 0) + 1
  end
end, "cr")

-- the code to debug starts here
local function DoSomethingMore(x)
  x = x / 2
end

local function DoSomething(x)
  x = x + 1
  if x % 2 then DoSomethingMore(x) end
end

for outer=1,100 do
  for inner=1,1000 do
    DoSomething(inner)
  end
end

-- the code to debug ends here; reset the hook
debug.sethook()

-- print the results
for f,time in pairs(total) do
  print(("Function %s took %.3f seconds after %d calls"):format(f, time, calls[f]))
end
