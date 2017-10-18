#!/usr/bin/env
# coding=utf-8

"""
>>> from static_meth import *
>>> x = Spam()
>>> y1, y2 = Sub(), Sub()
>>> z1, z2, z3 = Other(), Other(), Other()
>>> x.numInstances, y1.numInstances, z1.numInstances
(6, 6, 6)
>>> Spam.numInstances, Sub.numInstances, Other.numInstances
(6, 6, 6)
"""

class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances = Spam.numInstances + 1

    @staticmethod
    def printNumInstances():
        print("Number of instances: ", Spam.numInstances)

class Sub(Spam):
    @staticmethod
    def printNumInstances():
        print('Extra stuff')
        Spam.printNumInstances()

class Other(Spam): pass
