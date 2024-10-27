import math

T = int(input())

for i in range(T):
    
    X,Y = map(int,input().split())
    
    if(X>=Y):
        print(0)
        
    else:
        print (math.ceil((Y-X)/8))


'''  "Chess Ratings":-

Alice has recently started playing Chess. Her current rating is X. She noticed that when she wins a game, her rating increases by 8 points.Can you help Alice in finding out the minimum number of games she needs to win in order to make her rating greater than or equal to Y?


"Input Format":-
The first line of input will contain an integer T — the number of test cases. The description of T test cases follows.
The first line of each test case contains two integers X andY, as described in the problem statement.

"Output Format":-
For each test case, output the minimum number of games that Alice needs to win in order to make her rating greater than or equal to Y.'''