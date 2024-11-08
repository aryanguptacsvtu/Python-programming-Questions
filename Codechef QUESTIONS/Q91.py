# cook your dish here
T = int(input())

for i in range(T):
    
    N = int(input())
    
    fact = 1

    for j in range(1,N+1):
        fact = fact*j
        
    print(fact)


'''     "Small Factorial":-
Write a program to find the factorial value of any number entered by the user.


"Input Format":-
The first line contains an integer T, the total number of testcases. Then T lines follow, each line contains an integer N.

"Output Format":-
For each test case, display the factorial of the given number N in a new line.'''