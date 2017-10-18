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

    @property
    def name(self):             # name = property(name)
        "name property docs"
        print('fetch...')
        return self._name
    @name.setter
    def name(self, value):      # name = name.setter(name)
        print('change...')
        self._name = value
    @name.deleter
    def name(self):             # name = name.deleter(name)
        print('remove...')
        del self._name
