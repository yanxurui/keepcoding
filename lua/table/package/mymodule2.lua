local P = {}
-- 使用全局变量来暴露package
-- 这种写法在项目中非常不推荐
-- mymodule = P
local function private()
    print("in private function")
end

function P.foo()
    print("Hello Lua!")
end

function P.bar()
    private()
    P.foo() -- need to prefix function call with module
end

return P
