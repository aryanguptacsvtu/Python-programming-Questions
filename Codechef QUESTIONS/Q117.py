class PrimeIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        while not self.is_prime(self.current):
            self.current += 1
        if self.current > self.limit:
            raise StopIteration
        return self.current

    def is_prime(self, num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True


'''     "Implement Prime Iterator":-

Create a Python class called PrimeIterator that generates prime numbers. Your task is to implement the PrimeIterator class so that it can be used as an iterator to generate prime numbers up to a given limit.

Your class should have the following methods:

__init__(self, limit): Initializes the iterator with a limit limit, which represents the upper bound for prime numbers generation.
__iter__(self): Returns the iterator object itself.
__next__(self): Generates the next prime number in the sequence.'''