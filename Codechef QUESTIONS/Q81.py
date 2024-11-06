# cook your dish here
T = int(input())

for i in range(T):
    
    X,Y = map(int, input().split())
    
    A_to_B = 500-(2*X) + (1000-(4*(X+Y)))
    B_to_A = 500-(2*(X+Y)) + (1000-(4*(Y)))
    
    if(A_to_B >= B_to_A):
        print(A_to_B)
        
    else:
        print(B_to_A)


'''     "A or B":-

There are two problems in a contest.
Problem A is worth 500 points at the start of the contest.
Problem B is worth 1000 points at the start of the contest.
Once the contest starts, after each minute:
Maximum points of Problem A reduce by 2 points .
Maximum points of Problem B reduce by 4 points.
It is known that Chef requires X minutes to solve Problem A correctly and Y minutes to solve Problem B correctly.


"Input Format":-
First line will contain T, number of test cases. Then the test cases follow.
Each test case contains of a single line of input, two integers X and Y - the time required to solve problems A and B in minutes respectively.

"Output Format":-
For each test case, output in a single line, the maximum number of points Chef can score if he optimally decides the order of attempting both the problems.'''