#!/usr/bin/env

class GetAttr(object):
    """
    >>> X = GetAttr()
    >>> print(X.attr1)
    1
    >>> print(X.attr2)
    2
    >>> print(X.attr3)
    get: attr3
    3
    >>> print(X.attr4)
    get: attr4
    3
    """
    attr1 = 1
    def __init__(self):
        self.attr2 = 2
    def __getattr__(self, attr):      # on undefined attrs only
        print('get: ' + attr)
        return 3

class GetAttribute(object):
    """
    >>> X = GetAttribute()
    >>> print(X.attr1)
    get: attr1
    1
    >>> print(X.attr2)
    get: attr2
    2
    >>> print(X.attr3)
    get: attr3
    3
    >>> print(X.attr4)
    Traceback (most recent call last):
        ...
    AttributeError: 'GetAttribute' object has no attribute 'attr4'
    """
    attr1 = 1
    def __init__(self):
        self.attr2 = 2
    def __getattribute__(self, attr): # on all attr fetches
        print('get: ' + attr)
        if attr == 'attr3':
            return 3
        else:
            return object.__getattribute__(self, attr) # use superclass to avoid looping here
