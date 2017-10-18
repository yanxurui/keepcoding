#!/usr/bin/env

class Spam(object):
    """
    >>> obj = Spam()
    >>> obj.imeth(1)
    1
    >>> Spam.imeth(obj, 2)
    2
    >>>
    >>> Spam.smeth(3)
    3
    >>> obj.smeth(4)
    4
    >>>
    >>> Spam.cmeth(5)
    (<class 'methods.Spam'>, 5)
    >>> obj.cmeth(6)
    (<class 'methods.Spam'>, 6)
    """
    def imeth(self, x):
        print(x)

    @staticmethod
    def smeth(x):
        print(x)

    @classmethod
    def cmeth(cls, x):
        print(cls, x)
