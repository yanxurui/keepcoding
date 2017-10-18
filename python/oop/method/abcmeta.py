from abc import ABCMeta, abstractmethod
class Super:
    """[summary]

    >>> X = Super()
    Traceback (most recent call last):
    TypeError: Can't instantiate abstract class Super with abstract methods action

    """
    __metaclass__ = ABCMeta

    def delegate(self):
        self.action()

    @abstractmethod
    def action(self):
        pass


class Sub1(Super):
    """[summary]

    >>> X = Sub1()
    Traceback (most recent call last):
    TypeError: Can't instantiate abstract class Sub1 with abstract methods action

    Extends:
        Super
    """

class Sub2(Super):
    """[summary]

    >>> X = Sub2()
    >>> X.delegate()
    spam

    Extends:
        Super
    """
    def action(self):
        print('spam')
