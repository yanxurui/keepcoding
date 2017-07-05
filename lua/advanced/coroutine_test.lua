-- 3 states: suspended, running, dead
print('-----states------')
local co = coroutine.create(function ()
    print("hi")
end)

print(coroutine.status(co))

coroutine.resume(co)

print(coroutine.status(co))


print('-----yield------')

co = coroutine.create(function ()
    for i=1,10 do
        print("co", i)
        coroutine.yield()
    end
end)

coroutine.resume(co)

print(coroutine.status(co))

for i = 2,12 do
    print(coroutine.resume(co))
end


print('-----exchange data ------')
-- The first resume, which has no corresponding yield waiting for it, 
-- passes its extra arguments as arguments to the coroutine main function
co = coroutine.create(function (a,b,c)
    print("co", a,b,c)

    print("co", coroutine.yield(
        math.min(a,b,c),
        math.max(a,b,c)
        )
    )
end)
print(coroutine.resume(co, 1, 2, 3))
--> co  1  2  3
--> true 1 3

print(coroutine.resume(co, "hello"))
---> co      hello
---> true


print('-----resume 2 coroutines ------')
local co1 = coroutine.create(function ()
    -- do something here
    -- waiting
    local name = coroutine.yield()
    print('hello, '..name)
end)

local co2 = coroutine.create(function (name)
    local name = coroutine.yield()
    print('goodbye, '..name)
end)

-- start
coroutine.resume(co1)
coroutine.resume(co2)

-- wake up
coroutine.resume(co1, 'yxr')
coroutine.resume(co2, 'yxr')

