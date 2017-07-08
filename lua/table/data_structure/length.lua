-- #返回从1开始非nil值的元素数

t={1,2,3}
print(#t)
--> 3

t[-1]=-1
t[0]=0
print(#t)
--> 3

t[5] = 5
print(#t)
--> 3

t['a'] = 'aaa'
print(#t)
--> 3


function tablelength(T)
  local count = 0
  for _ in pairs(T) do count = count + 1 end
  return count
end
print(tablelength(t))
--> 7
