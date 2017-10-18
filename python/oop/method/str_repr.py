class Spam(object):
    """[summary]

    >>> X = Spam(13)
    >>> X
    __repr__: 13
    >>> print(X)
    __str__: 13
    >>> [X, X]
    [__repr__: 13, __repr__: 13]
    """
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return '__str__: %s' % self.data

    def __repr__(self):
        return '__repr__: %s' % self.data
