-- new windows inherit any absent field from a prototype window

-- create a namespace
Window = {}
-- create the prototype with default values
Window.prototype = {x=0, y=0, width=100, height=100}
-- create a metatable
Window.mt = {}
-- declare the constructor function
function  Window.new(o)
    setmetatable(o, Window.mt)
    return o
end

Window.mt.__index = function(table, key)
    return Window.prototype[key]
end
-- 上面的__index元方法等价于
-- Window.mt.__index = Window.prototype

w = Window.new{x=10, y=20}
print(w.width) --> 100
print(rawget(w, width)) --> nil
