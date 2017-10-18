#!/usr/bin/env
# coding=utf-8

"""
>>> sue = Person('sue', 10000)
>>> print(sue)
[Person: sue, 10000]
>>> sue.giveRaise(.1)
>>> print(sue)
[Person: sue, 11000]
>>> Person.giveRaise(sue, .1)
>>> print(sue)
[Person: sue, 12100]
>>>
>>> tom = Manager('tom', 20000)
>>> tom.giveRaise(.1)
>>> print(tom)
[Person: tom, 24000]
"""
class Person(object):
    # 类属性在class语句中通过赋值语句添加
    base = 1000

    # 构造函数
    def __init__(self, name, pay=0):
        # 实例属性在方法中通过对self进行赋值添加
        self.name = name
        if pay < self.base:
            pay = self.base
        self.pay = pay
    
    # 方法，第一个参数自动填充为调用该函数的对象
    def giveRaise(self, percent):
        self.pay = int(self.pay*(1 + percent))
    
    # 运算符重载方法
    def __str__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)


# Manager继承Person
# Manager是子类，Person是超类
class Manager(Person):
    def giveRaise(self, percent, bonus=0.1):
        # self.giveRaise会被解析为Manager.giveRaise，造成死循环
        Person.giveRaise(self, percent + bonus)

# 一个python文件是一个模块，模块也是对象
# 当作为脚本运行的时候模块的__name__属性的值是__main__
# 而当它作为一个模块被导入的时候__name__是模块名，也就是文件名（不包含后缀）
if __name__ == '__main__':
    sue = Person('sue', 10000)
    print(sue)
    sue.giveRaise(.1)
    print(sue)
    # 通过类调用实例方法
    Person.giveRaise(sue, .1)
    print(sue)

    tom = Manager('tom', 20000)
    tom.giveRaise(.1)
    print(tom)

