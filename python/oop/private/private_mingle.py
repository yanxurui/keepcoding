class C1(object):
    def meth1(self): self.__X = 88      # X is mine, becomes _C1__X
    def meth2(self): print(self.__X)

class C2(object):
    def metha(self): self.__X = 99      # X is mine, becomes _C2__X
    def methb(self): print(self.__X)

class C(C1, C2):
    """[summary]

    >>> c = C()
    >>> c.meth1()
    >>> c.metha()
    >>> c.meth2()
    88
    >>> c.methb()
    99
    >>> c.__dict__
    {'_C2__X': 99, '_C1__X': 88}

    Extends:
        C1
        C2

    Variables:
        pass {[type]} -- [description]
    """
    pass

