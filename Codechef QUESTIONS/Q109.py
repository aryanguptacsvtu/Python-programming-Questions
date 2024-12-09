counter = 0

def increment_global_counter(arr):
    global counter
    counter += sum(arr)
    return counter

# Initial value of global counter is 0
print("Initial global counter:", counter)

# Increment global counter by the sum of elements in the array [5, 10, 15]
increment_global_counter([5, 10, 15])
print("After incrementing by the sum of array elements:", counter)  

# Increment global counter by the sum of elements in the array [2, 4, 6, 8]
increment_global_counter([2, 4, 6, 8])
print("After incrementing by the sum of array elements:", counter)  


'''   "Increment Global Counter" :-

You are tasked with implementing a Python function called increment_global_counter. This function should increment a global counter variable named counter by the sum of all the elements of an array passed as an argument to the function. The global counter variable should be initialized with 0 initially.'''