-- create private index
local index = {}

-- create metatable
local mt = {
  __index = function (t,k)
    print("*access to element " .. tostring(k))
    return t[index][k]   -- access the original table
  end,

  __newindex = function (t,k,v)
    print("*update of element " .. tostring(k) ..
                         " to " .. tostring(v))
    t[index][k] = v   -- update original table
  end
}

function track (t)
  local proxy = {}
  proxy[index] = t
  setmetatable(proxy, mt)
  return proxy
end


-- original table
t = {}
t = track(t)
t[2] = 'hello'
print(t[2])

-- unfortunately, pairs will not traverse the original table
for k,v in pairs(t) do
  print(k,v)
end
-- a private key that nobody else can access
print(t[{}])
