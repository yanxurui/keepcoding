a = {}
b = {}
setmetatable(a, b)
b.__mode = "k"         -- now `a' has weak keys
key = {}               -- creates first key
a[key] = 1
key = {}               -- creates second key
a[key] = 2
for k, v in pairs(a) do print(v) end

collectgarbage()       -- forces a garbage collection cycle
for k, v in pairs(a) do print(v) end
--> 2
