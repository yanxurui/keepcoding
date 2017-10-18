class A(object):
    """
    >>> a = A('foo')
    >>> # you can still access them directly but don't do this
    >>> a._spam()
    I am foo
    >>> print(a._name)
    foo
    """

    def __init__(self, name):
        self._name = name

    def _spam(self):
        print('I am %s' % self._name)
