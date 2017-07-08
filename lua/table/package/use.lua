-- 包名和文件名没有对应关系
-- require "mymodule1"的作用就是执行mymodule1.lua，返回一个表示包的table
-- 在实际脚本中，mymodule通常是局部变量
mymodule = require "mymodule1"
mymodule.foo()
mymodule.bar()
print("---------------")
mymodule = require "mymodule2"
mymodule.foo()
mymodule.bar()
