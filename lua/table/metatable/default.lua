local key = {}    -- unique key
local mt = {__index = function (t) return t[key] end}
function setDefault (t, d)
  t[key] = d
  setmetatable(t, mt)
end

tab = {x=10, y=20}
print(tab.x, tab.z)     --> 10   nil
setDefault(tab, 0)
print(tab.x, tab.z)     --> 10   0


-- another implemention by key weak table
local defaults = {}    -- unique key
setmetatable(defaults, {__mode = "k"})
local mt = {__index = function (t) return defaults[t] end}
function setDefault2 (t, d)
  defaults[t] = d
  setmetatable(t, mt)
end



tab = {x=10, y=20}
print(tab.x, tab.z)     --> 10   nil
setDefault(tab, 0)
print(tab.x, tab.z)     --> 10   0


tab = {x=10, y=20}
print(tab.x, tab.z)     --> 10   nil
setDefault2(tab, 0)
print(tab.x, tab.z)     --> 10   0
