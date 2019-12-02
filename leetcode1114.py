class Foo:
    def __init__(self):
        self.mutex = 1  
        pass


    def first(self, printFirst: 'Callable[[], None]') -> None:
        while self.mutex != 1:
            pass
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.mutex = 2


    def second(self, printSecond: 'Callable[[], None]') -> None:
        while self.mutex != 2:
            pass
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.mutex = 3


    def third(self, printThird: 'Callable[[], None]') -> None:
        while self.mutex != 3:
            pass
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        self.mutex = 0
