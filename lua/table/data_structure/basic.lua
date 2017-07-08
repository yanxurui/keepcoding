-- 创建table的唯一方式是使用constructor表达式
-- 最简单的形式就是{}，每次都会创建一个新的table
a = {}

-- 同一个table中的健和值可以是任何nil以外的值，包括function和其他table
a["x"] = "x"
a[-1] = -1
a[true] = true
print(a["x"]) -->x
-- 没有赋值的健对应nil
print(a["y"]) -->nil
print(a[-1]) -->-1
print(a[true]) -->true
-- 赋值为nil可以删除某个健
a[true] = nil
-- lua提供的语法糖：a.name等价于a["name"]
-- 不要把a.x和a[x]混淆
print(a.x) -->x

-- 0和'0'在表中代表不同的健，一定要小心否则很容易引入bug
a[0] = 'integer 0'
a['0'] = 'string 0'
print(a[0]) -->integer 0
print(a['0']) -->string 0



-- 在lua中，table是对象
a = {}
-- 对象通过引用来操作，不会发生拷贝
-- a和b指向同一个对象
b = a
print(b == a) -->true
b["x"] = "y"
print(a["x"]) -->y
-- a还在引用该table，如果一个table没有引用的时候，lua会删掉它并收回内存
b = nil
print(a["x"]) -->y
-- 创建两个独立的对象
t1 = {}
t2 = {}
-- t1和t2引用不同的对象
print(t1 == t2) -->false
a={}
a[t1] = 1
print(a[t2]) -->nil





-- constructor提供了两种创建table的形式
-- list-style
{"red", "green", "blue"}

-- record-style
{x=0, y=0}
-- 等价于
a = {}; a.x=0; a.y=0

-- 两种写法可以混合起来用
-- 可以嵌套，one的索引是1，two的索引是2，不受record的影响
{"one", x={1,'x'}, y=2, "two"}

-- 当健不是字符串或是某些特殊字符的时候，需要将健写成表达式——用[]扩起来
opnames = {[0] = 0, ["+"] = "add"}
-- 上面的list-style和record-style例子分别等价于以下写法
{[1]="red", [2]="green", [3]="blue"}
{["x"]=0, ["y"]=0}

-- ,也可以用代替;替代，常用来分割不同的部分
-- 末尾出现,也是允许的
{x=10, y=45; "one", "two", "three",}



-- functions are first-class values, they can be stored in table
a = {}
a.foo = function (x,y) return x + y end
print(a.foo(1,2)) -->3
-- another syntax to define such functions
function a.bar(x,y)
	return x*y
end
print(a.bar(2,3)) -->6

