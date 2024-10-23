T = int(input())

for i in range(T):
    
    X,Y = map(int,input().split())
    
    if(0.5*X<= Y):
        print("YES")
        
    else:
        print("NO")


'''  "Expert Setter":-

A problem setter is called an expert if at least 50% of their problems are approved by Chef.
Munchy submitted X problems for approval. If Y problems out of those were approved, find whether Munchy is an expert or not.

"Input Format":-
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of a two space-separated integers X and Y - the number of problems submitted and the number of problems that were approved by Chef.

"Output Format":-
For each test case, output on a new line YES, if Munchy is an expert. Otherwise, print NO.
The output is case-insensitive. Thus, the strings YES, yes, yeS, and Yes are all considered the same.'''