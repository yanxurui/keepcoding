-- 默认没有元表
t = {}
print(getmetatable(t))   --> nil

-- 调用setmetatable设置元表
t1 = {}
setmetatable(t, t1)
assert(getmetatable(t) == t1)
