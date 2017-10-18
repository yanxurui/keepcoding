# http://python3-cookbook.readthedocs.io/zh_CN/latest/c08/p07_calling_method_on_parent_class.html

class Base(object):
    def __init__(self):
        print('Base.__init__')

class A(Base):
    def __init__(self):
        super(A, self).__init__()
        print('A.__init__')

class B(Base):
    def __init__(self):
        super(B, self).__init__()
        print('B.__init__')

class C(A, B):
    """[summary]
    >>> C.__mro__               
    (<class 'super_example_complex.C'>, <class 'super_example_complex.A'>, <class 'super_example_complex.B'>, <class 'super_example_complex.Base'>, <type 'object'>)
    >>> c = C()
    Base.__init__
    B.__init__
    A.__init__
    C.__init__

    Extends:
        A
        B
    """
    def __init__(self):
        super(C, self).__init__()  # Only one call to super() here
        print('C.__init__')
