-- define an object with a method
Account = {balance = 100}
function Account.deposit (self, v)
  self.balance = self.balance + v
end

-- an equivalent form
--  self can be omitted by the colon syntax
-- function Account:deposit (v)
--   self.balance = self.balance - v
-- end

-- call the method
Account.deposit(Account, 0)
print(Account.balance)

-- the same
Account:deposit(100)
print(Account.balance)
