Set = {}
Set.mt = {} -- metatable

function Set.new(t)
    local set = {}
    setmetatable(set, Set.mt) --
    for _, l in ipairs(t) do set[l] = true end
    return set
end


-- Arithmetic Metamethods
-- 并集
function Set.union(a,b)
    local res = Set.new{}
    for k in pairs(a) do res[k] = true end
    for k in pairs(b) do res[k] = true end
    return res
end

-- 交集
function Set.intersection(a,b)
    local res = Set.new{}
    for k in pairs(a) do
        res[k] = b[k]
    end
    return res
end

Set.mt.__add = Set.union -- __add元方法支持+运算
Set.mt.__mul = Set.intersection -- __mul元方法支持*运算


-- Relational Metamethods
-- 集合包含
Set.mt.__le = function (a,b)
    for k in pairs(a) do
        if not b[k] then return false end
    end
    return true
end

-- 真子集
Set.mt.__lt = function(a,b)
    return a <= b and not( b <= a)
end

-- 相等
Set.mt.__eq = function (a,b)
    return a <= b and b <= a
end


-- Library-Defined Metamethods
-- 支持print打印set
-- print函数总是会调用tostring函数格式化输出
-- 当tostring格式化一个对象的时候，会调用对象的__tostring元方法
Set.mt.__tostring = function(set)
    local s = "{"
    local sep = ""
    for e in pairs(set) do
        s = s .. sep .. e
        sep = ", "
    end
    return s .. "}"
end


-- Test --
s1 = Set.new{10, 20, 30, 50}
s2 = Set.new{10, 20, 40}
print(s1)
print(s2)
s3 = s1 + s2
print(s3)
s3 = s1 * s2
print(s3)

-- lua进行+运算时
-- 如果左操作数有__add元方法，则使用左右两个操作数作为参数调用该方法
-- 否则，如果右操作数有__add元方法，就调用该方法
-- 否则，出错
-- 下面的例子会调用Set的元方法Set.union，同样的10 + s and "hy" + s也会调用该方法，因为number和string都没有__元方法
s = Set.new{1,2,3}
s = s + 8

-- 我们的实现会在pairs的时候出错，所以需要显示的检查类型
function Set.union(a,b)
    if getmetatable(a) ~= Set.mt or
       getmetatable(b) ~= Set.met then
      error("attempt to `add` a set with a non-set value", 2)
    end
    local res = Set.new{}
    for k in pairs(a) do res[k] = true end
    for k in pairs(b) do res[k] = true end
    return res
end
-- 需要重新设置元方法
Set.mt.__add = Set.union
print(10 + s)
print("hy" + s)



s1 = Set.new{2, 4}
s2 = Set.new{4, 10, 2}
print(s1 <= s2)       --> true
print(s1 < s2)        --> true
print(s1 >= s1)       --> true
print(s1 > s1)        --> false


-- 关系运算不支持混合类型
-- 如果两个对象的关系运算元方法不一样，比较运算会出错，与10 <= "10" 的行为一致
-- 相等比较是个例外，不会出错但结果是false
print(s1 == s2 * s1)  --> true
