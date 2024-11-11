# cook your dish here
T = int(input())

for i in range(T):
    
    N = int(input())
    a = list(map(int, input().split()))
    
    degree = 0
    
    for i in range(N):
        
        if a[i]!=0 and i>degree:
            degree=i
            
    print(degree)


'''     "Degree of Polynomial":-

In mathematics, the degree of polynomials in one variable is the highest power of the variable in the algebraic expression with non-zero coefficient.Find the degree of the polynomial.
Note: It is guaranteed that there exists at least one term with non-zero coefficient.


"Input Format":-
First line will contain T, number of test cases. Then the test cases follow.
First line of each test case contains of a single integer N - the number of terms in the polynomial.
Second line of each test case contains of N space-separated integers - the ith integer Ai-1 corresponds to the coefficient of xi-1.

"Output Format":-
For each test case, output in a single line, the degree of the polynomial.'''