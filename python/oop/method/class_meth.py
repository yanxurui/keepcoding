#!/usr/bin/env
# coding=utf-8

"""
>>> x = Spam()
>>> y1, y2 = Sub(), Sub()
>>> z1, z2, z3 = Other(), Other(), Other()
>>> x.numInstances, y1.numInstances, z1.numInstances
(1, 2, 3)
>>> Spam.numInstances, Sub.numInstances, Other.numInstances
(1, 2, 3)
"""

class Spam:
    numInstances = 0
    @classmethod
    def count(cls):
        cls.numInstances += 1
    def __init__(self):
        self.count()

class Sub(Spam):
    numInstances = 0
    def __init__(self):
        Spam.__init__(self)

class Other(Spam):
    numInstances = 0
