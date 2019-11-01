from threading import Lock

class Foo:
    def __init__(self):
        l1 = Lock()
        l2 = Lock()
        l1.acquire()
        l2.acquire()
        self.l1 = l1
        self.l2 = l2

    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.l1.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        with self.l1:
            printSecond()
            self.l2.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        with self.l2:
            printThird()
