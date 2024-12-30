class FibonacciIterator:
    def __init__(self):
        self.prev = 0
        self.curr = 1

    def __iter__(self):
        return self

    def __next__(self):
        fib = self.prev
        self.prev, self.curr = self.curr, self.prev + self.curr
        return fib
    

'''     "Implement Fibonacci Iterator":-

You are tasked with implementing an iterator to generate Fibonacci numbers. Write a class FibonacciIterator which behaves as an iterator without using any external library or generator functions. The iterator should yield Fibonacci numbers indefinitely.

FibonacciIterator class must have the following methods:

init(self): Initializes the iterator.
iter(self): Returns the iterator object.
next(self): Returns the next Fibonacci number.'''