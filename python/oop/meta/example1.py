#!/usr/bin/env
# coding=utf-8

def required():
    return True

def extra(self, arg):
    print(arg)

# config class based on some runtime test
class Extras(type):
    def __init__(Class, classname, superclasses, attributedict):
        if required():
            Class.extra = extra

class Client1():
    __metaclass__ = Extras

X = Client1() # X is instance of Client1
X.extra('hello')
