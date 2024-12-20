my_list = [1, 2, 3, 4, 5]

# Get an iterator for the list
my_iter = iter(my_list)

# Print each element of the list using the iterator
print(next(my_iter))  # Output: 1
print(next(my_iter))  # Output: 2
print(next(my_iter))  # Output: 3
print(next(my_iter))  # Output: 4
print(next(my_iter))  # Output: 5

list = [10, 20, 32, 44, 55]

# Using iterator with a for loop
for item in iter(list):
    print(item)

'''     "Iterators in Python":-
In Python, an iterator is an object that allows iteration over a sequence of elements. It provides a way to access elements of a container one by one without needing to know the underlying structure of the containe'''