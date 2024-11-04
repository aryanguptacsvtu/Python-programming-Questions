# cook your dish here
import math
T = int(input())

for i in range(T):
    
    X = int(input())
    
    if((X%5 !=0) and (X%10 !=0)):
        print(-1)
        
    elif((X%5==0 )and (X%10!=0)):
        print(math.ceil(X//10)+1)
        
    else:
        print(X//10)
    
    
'''    "Minimum number of coins":-

Chef has infinite coins in denominations of rupees 5 and rupees 10.
Find the minimum number of coins Chef needs, to pay exactly X rupees. 


"Input Format":-
First line will contain T, number of test cases. Then the test cases follow.
Each test case contains of a single integer X.

"Output Format":-
For each test case, print a single integer - the minimum number of coins Chef needs, to pay exactlyX rupees. If it is impossible to pay X rupees in denominations of rupees 5 and 10 only, print -1.'''