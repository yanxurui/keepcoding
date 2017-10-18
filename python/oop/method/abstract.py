class Super(object):
    """[summary]

    >>> X = Super()
    >>> X.delegate()
    Traceback (most recent call last):
    NotImplementedError: action must be defined!

    """
    def delegate(self):
        self.action()

    def action(self):
        raise NotImplementedError('action must be defined!')

class Sub1(Super):
    """[summary]

    >>> s1 = Sub1()
    >>> s1.delegate()
    Traceback (most recent call last):
    NotImplementedError: action must be defined!

    """
    pass

class Sub2(Super):
    """[summary]

    >>> s2 = Sub2()
    >>> s2.delegate()
    spam

    Extends:
        Super
    """
    def action(self):
        print('spam')
