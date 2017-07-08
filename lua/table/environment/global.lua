print(_ENV == _G) -- prints true, since the default _ENV is set to the global table

a = 1

local function f(t)
  -- since we will change the environment, standard functions will not be visible
  local print = print
  -- change the environment. without the local, this would change the environment for the entire chunk
  local _ENV = t
  -- prints nil, since global variables (including the standard functions) are not in the new env
  print(getmetatable)
  -- create a new entry in t, doesn't touch the original "a" global
  a = 2
  b = 3
end

local t = {}
f(t)

print(a, b) --> 1 nil
print(t.a, t.b) --> 2 3
