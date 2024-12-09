def counter_generator():
    count = 0  # Counter variable in the enclosing scope
    
    def counter():
        nonlocal count  # Declare count as non-local
        count += 1
        return count
    
    return counter


''' "Counter Generator Coding Problem":-

You are tasked with implementing a counter_generator function in Python. The function should generate and return another function, called counter, which, when called, increments count variable.

The count variable must be declared in the counter_generator method. The initial value of the count variable should be 0 for each instance of the counter.'''