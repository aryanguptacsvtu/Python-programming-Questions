# cook your dish here
import math

T = int(input())

for i in range(T):
    
    A, B, K = map(int,input().split())
    
    if(A==B):
        print(0)
        
    elif(A<B):
        steps = math.ceil((B-A)/K)
        print(steps)
    
    else:
        steps = math.ceil((A-B)/K)
        print(steps)


'''     "Reach fast":-

Chef is standing at coordinate A while Chefina is standing at coordinate B.
In one step, Chef can increase or decrease his coordinate by at most K.


"Input Format":-
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of three integers A,B, and K, the initial coordinate of Chef, the initial coordinate of Chefina and the maximum number of coordinates Chef can move in one step.

"Output Format":-
For each test case, output the minimum number of steps required by Chef to reach Chefina.'''