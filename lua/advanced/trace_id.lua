function tablelength(T)
  local count = 0
  for _ in pairs(T) do count = count + 1 end
  return count
end

s = os.clock()
t = {}

for i = 1,1000000 do
	-- t[math.random(10000000,99999999)]=1
	t[string.format('%d', math.random(10000000,99999999))]=1
end

print(os.clock()-s)
print(tablelength(t))


print('--------')


s = os.clock()
t = {}

for i = 1,1000000 do
  -- local token = string.format("%s", os.date("%Y-%m-%d %H:%M:%S"))
  local intpart, decpart = math.modf(os.clock())
  local token = string.format("%s,%f",
  	os.date("%Y-%m-%d %H:%M:%S"),
  	decpart
  	)
  t[token] = 1
end

print(os.clock()-s)
print(tablelength(t))
