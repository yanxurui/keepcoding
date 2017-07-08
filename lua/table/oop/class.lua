Account = {balance = 100}
function Account:new (o)
  o = o or {}   -- create object if user does not provide one
  setmetatable(o, self)
  self.__index = self
  return o
end
function Account.deposit (self, v)
  self.balance = self.balance + v
end

a = Account:new{balance = 0}
-- a中没有deposit，所以就到a的metatable的__index中去查找，
-- a的metatable是Account，Account的__index是Account本身，
-- Account中定义了deposit，所以最终调用了Account.deposit(a, 100.00)，
-- 也就是a.balance = a.balance + v，因为self此时是a
a:deposit(100.00)
-- 属性的继承与方法完全一样
print(a.balance)
