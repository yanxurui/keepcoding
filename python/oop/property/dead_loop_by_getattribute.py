#!/usr/bin/env

class BadGetAttribute(object):
    def __init__(self):
        self.a = 'I am a'
    def __getattribute__(self, name):
        print('get: ' + name)
        return self.other

class GoodGetAttribute(object):
    """
    >>> X = GoodGetAttribute()
    >>> X.a
    get: a
    'I am a'
    """
    def __init__(self):
        self.a = 'I am a'
    def __getattribute__(self, name):
        print('get: ' + name)
        return object.__getattribute__(self, name)

class GoodSetAttribute(object):
    """
    >>> X = GoodSetAttribute()
    set: a = I am a
    >>> X.a = 'A'
    set: a = A
    >>> X.a
    'A'
    """
    def __init__(self):
        self.a = 'I am a'
    def __setattr__(self, name, value):
        print('set: %s = %s' % (name, value))
        self.__dict__[name] = value

