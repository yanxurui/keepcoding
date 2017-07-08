function newAccount (initialBalance)
  -- private properties
  local self = {balance = initialBalance}
  -- private method
  local format = function (balance) return "$" .. balance end
  local getBalance = function () return format(self.balance) end
  -- interface
  return {
    deposit = deposit,
    getBalance = getBalance
  }
end
a = newAccount(100)
print(a.getBalance())
