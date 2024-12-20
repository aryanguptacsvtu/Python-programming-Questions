def my_generator():
    yield 1
    yield 2
    yield 3

# Create a generator object
gen = my_generator()

# Iterate over the generator using a for loop
for value in gen:
    print(value)


'''   "How to use for loop in generator functions":-

In Python, you can use a for loop to iterate over the values produced by a generator function. When you use a for loop with a generator, the loop iterates over the values yielded by the generator one at a time, without needing to explicitly call the next() function.'''