#!/usr/bin/env

class Person(object):
    """
    >>> bob = Person('Bob Smith')
    >>> print(bob.name)
    fetch...
    Bob Smith
    >>> bob.name = 'Robert Smith'
    change...
    >>> print(bob.name)
    fetch...
    Robert Smith
    >>> del bob.name
    remove...
    """
    def __init__(self, name):
        self._name = name

    def __getattr__(self, attr):
        if attr == 'name':
            print('fetch...')
            return self._name
        else:
            raise AttributeError(attr)
    def __setattr__(self, attr, value):
        if attr == 'name':
            print('change...')
            attr = '_name'
        self.__dict__[attr] = value
    def __delattr__(self, attr):
        if attr == 'name':
            print('remove...')
            attr = '_name'
        del self.__dict__[attr]
