#!/usr/bin/env

class Name(object):
    "name descriptor docs"
    def __get__(self, instance, owner):
        print('fetch...')
        return instance._name
    def __set__(self, instance, value):
        print('change...')
        instance._name = value
    def __delete__(self, instance):
        print('remove...')
        del instance._name

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
    name = Name()
