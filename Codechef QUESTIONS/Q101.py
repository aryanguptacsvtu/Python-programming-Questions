# cook your dish here
# "FIRST METHOD" :-
T = int(input())

for i in range(T):
    A1,A2,A3,B1,B2,B3 = map(int, input().split())
    
    Alice_score = A1+A2+A3 - min(A1,A2,A3)
    Bob_score  =  B1+B2+B3 - min(B1,B2,B3)
    
    if(Alice_score > Bob_score):
        print("Alice")
        
    elif(Alice_score < Bob_score):
        print("Bob")
        
    else:
        print("Tie")


# "SECOND METHOD":-
T = int(input())

for i in range(T):
    l = list(map(int,input().split()))

    alice = l[0:3]
    bob = l[3:6]
    alice.sort()
    bob.sort()

    if(alice[1] + alice[2] > bob[1] + bob[2]):
        print("Alice")

    elif(alice[1] + alice[2] < bob[1] + bob[2]):
        print("Bob")

    else:
        print("Tie")


'''      "Best of Two":-

Alice and Bob are playing a game. Each player rolls a regular six faced dice 3 times.
The score of a player is the sum of the values of the highest 2 rolls. The player with the highest score wins, and the game ends in a Tie if both players have the same score.Find the winner of the game or determine whether it is a tie.


"Input Format":-
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case contains six space-separated integers A1,A2,A3,B1,B2,B3 — the values Alice gets in her 3 dice rolls, followed by the values which Bob gets in his 3 dice rolls.

"Output Format":-
For each test case, output on a new line Alice if Alice wins, Bob if Bob wins and Tie in case of a tie.
Note that you may print each character in uppercase or lowercase. For example, the strings tie, TIE, Tie, and tIe are considered identical.
'''