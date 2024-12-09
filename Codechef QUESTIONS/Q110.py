def outer_function():
    x = 10  # Variable in the enclosing scope

    def inner_function():
        nonlocal x  # Declaring x as non-local
        x = 20  # Modifying the value of x from the enclosing scope
        print("Inside the inner function:", x)

    inner_function()
    print("Outside the inner function:", x)  # Accessing the modified value of x

outer_function()

'''     "Non-local Scope" :-

Non-local scope refers to the scope that lies between the local and global scopes, typically found in nested functions. It allows a nested function to access and modify variables in the enclosing (non-global) scope'''