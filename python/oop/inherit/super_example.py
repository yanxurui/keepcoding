# only works for new-style classes
class A(object):
    def spam(self):
        print('A.spam')

class B(A):
    """[summary]

    >>> b = B()
    >>> b.spam()
    B.spam
    A.spam

    Extends:
        A
    """

    def spam(self):
        print('B.spam')
        super(B, self).spam()  # Call parent spam(), can be replaced by super() in python3
