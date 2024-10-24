local function output(...)
    print(...)
end
output('hello', ' world')

local function output2(...)
    output(..., ' end')
end
output2('hello', ' world')
-- http://www.lua.org/manual/5.1/manual.html#2.5.9
-- If a vararg expression is used inside another expression or in the middle of a list of expressions, 
-- then its return list is adjusted to one element

-- how to pass varargs to another function in middle of argument list?
