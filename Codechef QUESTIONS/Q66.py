# cook your dish here
T = int(input())

for i in range(T):
    X,Y = map(int,input().split())

    moves = 0
    while X > 0:
        if X >= Y:
            moves =moves + (X // Y)
            X = X % Y
        else:
            moves = moves +X
            X = 0

    print(moves)


'''   "X Jumps":-

Chef is currently standing at stair 0 and he wants to reach stair numbered X.
Chef can climb either Y steps or 1 step in one move.
Find the minimum number of moves required by him to reach exactly the stair numbered X.


"Input Format":-
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of a single line of input containing two space separated integers X and 
Y denoting the number of stair Chef wants to reach and the number of stairs he can climb in one move.

"Output Format":-
For each test case, output the minimum number of moves required by him to reach exactly the stair numbered X.'''