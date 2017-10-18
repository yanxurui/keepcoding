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
    def getName(self):
        print("fetch...")
        return self._name
    def setName(self, value):
        print("change...")
        self._name = value
    def delName(self):
        print("remove...")
        del self._name
    name = property(getName, setName, delName, "name property docs")
