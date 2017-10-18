#!/usr/bin/env 

"""
>>> c1 = C1()
>>> c1.method()
method of a
>>> c2 = C2()
>>> c2.method()
method of b
"""
class A:
    def method(self):
        print('method of a')

class B:
    def method(self):
        print('method of b')

class C1(A,B):
    pass

class C2(B,A):
    pass
