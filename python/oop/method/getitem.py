class Spam(object):
    """[summary]

    >>> X = Spam()
    >>> X.data = 'Spam'
    >>> for i in X:
    ...     print(i)
    ...
    S
    p
    a
    m

    >>> [c for c in X]
    ['S', 'p', 'a', 'm']

    >>> 'p' in X
    True

    >>> list(map(str.upper, X))
    ['S', 'P', 'A', 'M']

    >>> a,b,c,d=X
    >>> a,c,d
    ('S', 'a', 'm')

    >>> tuple(X)
    ('S', 'p', 'a', 'm')
    """
    def __getitem__(self, i):
        return self.data[i]
