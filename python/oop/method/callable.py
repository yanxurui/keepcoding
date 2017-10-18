class Spam(object):
    """[summary]

    >>> X = Spam()
    >>> X('a', 'b', c='c')
    ('Called: ', ('a', 'b'), {'c': 'c'})
    """
    def __call__(self, *args, **kargs):
        print('Called: ', args, kargs)
