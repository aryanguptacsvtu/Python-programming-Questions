def factorial(n):
    if(n<=0):
        return 1
        
    else:
        return n* factorial(n-1)
    

t = int(input())

for i in range(t):
    
    n = int(input())
    
    print(factorial(n))


'''    "Small factorials":-
You are asked to calculate factorials of some small positive integers.

"Input Format":-
An integer t, 1<=t<=100, denoting the number of testcases, followed by t lines, each containing a single integer n, 1 <= n <= 100

"Output Format":-
For each integer n given at input, display a line with the value of n!
Note: For larger numbers, their factorial can overflows any available numeric data type in C.
'''