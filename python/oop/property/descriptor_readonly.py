#!/usr/bin/env

class D(object):
    def __get__(*args): print('get')
    def __set__(*args): raise AttributeError('cannot set')

class C(object):
    """
    >>> X = C()
    >>> X.a
    get
    >>> X.a = 100
    Traceback (most recent call last):
        ...
    AttributeError: cannot set
    """
    a = D()
