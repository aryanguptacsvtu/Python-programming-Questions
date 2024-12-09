# Global namespace variable
global_var = 10

def my_function():
    # Local namespace variable
    local_var = 20
    print("Inside the function - local_var:", local_var)
    print("Inside the function - global_var:", global_var)

my_function()

# Accessing global variable outside the function
print("Outside the function - global_var:", global_var)


#  "Namespaces in Python"