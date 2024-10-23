T = int(input())

for i in range(T):
    
    R1,R2,R3,R4 = map(int,input().split())
    
    if(R1==0 and R2==0 and R3==0 and R4==0):
        print("IN")
        
    else:
        print("OUT")


'''  "Chefland Games":-

In Chefland, a tennis game involves 4 referees.
Each referee has to point out whether he considers the ball to be inside limits or outside limits. The ball is considered to be IN if and only if all the referees agree that it was inside limits.
Given the decision of the 4 referees, help Chef determine whether the ball is considered inside limits or not.

"Input Format":-

The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of a single line of input containing R1,R2,R3,R4 denoting the decision of the respective referees.
Here R can be either 0 or 1 where 0 would denote that the referee considered the ball to be inside limits whereas 1 denotes that they consider it to be outside limits.'''