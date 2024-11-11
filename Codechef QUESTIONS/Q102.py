n = int(input())
play1 = 0
play2 = 0
max1 = 0
max2 = 0
for _ in range(n):
    a,b = map(int,input().split())

    max1 += a
    max2 += b

    if (max1 > max2):
        play1 = max(play1,max1-max2)
    else:
        play2 = max(play2,max2-max1)

if (play1 > play2):
    print(1,play1)

else:
    print(2,play2)
    

'''     "The Lead Game":-

The Siruseri Sports Club organises an annual billiards game where the top two players of Siruseri play against each other. The Manager of Siruseri Sports Club decided to add his own twist to the game by changing the rules for determining the winner. In his version, at the end of each round, the cumulative score for each player is calculated, and the leader and her current lead are found. Once all the rounds are over the player who had the maximum lead at the end of any round in the game is declared the winner.


"Input Format":-
The first line of the input will contain a single integer N (N ≤ 10000) indicating the number of rounds in the game. Lines 2,3,...,N+1 describe the scores of the two players in the N rounds. Line i+1 contains two integer Si and Ti, scores of the Player 1 and 2 respectively, in round i. You may assume that 1 ≤ Si ≤ 1000 & 1 ≤ Ti ≤ 1000.

"Output format":-
Your output must consist of a single line containing two integers W and L, where W is 1 or 2 and indicates the winner and L is the maximum lead attained by the winner.
'''
