-- paremt class
Account = {balance = 0}

function Account:new (o)
  o = o or {}
  setmetatable(o, self)
  self.__index = self
  return o
end

function Account:deposit (v)
  self.balance = self.balance + v
end

function Account:withdraw (v)
  if v > self.balance then error"insufficient funds" end
  self.balance = self.balance - v
end


-- subclass
SpecialAccount = Account:new()

-- redefine method
function SpecialAccount:withdraw (v)
  if v - self.balance >= self:getLimit() then
    error"insufficient funds"
  end
  self.balance = self.balance - v
end

-- add method
function SpecialAccount:getLimit ()
  return self.limit or 0
end

-- create an instance of SpecialAccout
-- SpecialAccount调用了从Account继承来的new方法，self是SpecialAccount。
-- 所以s的meltable是SpecialAccount，并且__index也是SpecialAccount，
-- 所以s直接继承了SpecialAccount类
s = SpecialAccount:new{limit=1000.00}
-- s中没有deposit方法，所以就到SpecialAccount类中查找，同样找不到，
-- 就到父类Account中查找，结果存在，所以就执行了Account类中定义的deposit方法
s:deposit(100.00)
-- s在SpecialAccount中找到了withdraw方法，就不会调用Account中的同名方法，
-- 也就是子类覆盖了父类中的同名方法
s:withdraw(200)
print(s.balance)
