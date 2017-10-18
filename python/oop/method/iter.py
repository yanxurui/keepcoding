class Spam(object):
    """[summary]

    >>> for i in Spam(1, 5):
    ...     print(i)
    ...
    1
    4
    9
    16

    >>> # iterate manully
    >>> X = Spam(1, 5)
    >>> I = iter(X)
    >>> next(I)
    1
    >>> next(I)
    4
    >>> next(I)
    9
    >>> next(I)
    16
    >>> next(I)
    Traceback (most recent call last):
    StopIteration
    """
    def __init__(self, start, stop):
        self.value = start
        self.stop = stop

    def __iter__(self):
        return self

    # use `def __next__(self)` in python3
    def next(self):
        if self.value == self.stop:
            raise StopIteration
        rv = self.value ** 2
        self.value += 1
        return rv

