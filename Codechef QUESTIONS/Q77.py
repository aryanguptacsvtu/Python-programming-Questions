# cook your dish here
T = int(input())

for i in  range(T):
    
    X,Y,D = map(int, input().split())
    
    diff = abs(X-Y)
    
    if(diff <= D):
        print("YES")
        
    else:
        print("NO")


'''      "Cup Finals":-
It is the World Cup Finals. Chef only finds a match interesting if the skill difference of the competing teams is less than or equal to D.
Given that the skills of the teams competing in the final are X and Y respectively, determine whether Chef will find the game interesting or not.


"Input Format":-
The first line of input will contain a single integer T, denoting the number of testcases. The description of T testcases follows.
Each testcase consists of a single line of input containing three space-separated integers X, Y, and D — the skill levels of the teams and the maximum skill difference.

"Output Format":-
For each testcase, output "YES" if Chef will find the game interesting, else output "NO" (without the quotes). The checker is case-insensitive, so "YeS" and "nO" etc. are also acceptable.'''