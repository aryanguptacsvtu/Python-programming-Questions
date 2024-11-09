# cook your dish here
T=int(input())

for i in range(T):
    n,a,b=map(int,input().split())
    count=0

    while n>1:
        count += 1 
        n = n/2
        
    print((count*a)+((count-1)*b))


'''
Binary Battles:-

In one round, each team will be paired up with and compete against one of the other teams. If there are X teams before the start of a round, X/2 matches are held simultaneously during the round between X/2 pairs of teams. The winning team of each match will move on to the next round, while the losing team of each match will be eliminated. There are no ties involved. The next round will then take place in the same format between the remaining teams.The process will continue until only one team remains, which will be declared the overall winner.
The organizers want to find the total time the event will take to complete. It is given that each round spans A minutes, and that there is a break of B minutes between every two rounds (no break after the last round).


"Input Format":-
The first line of input will contain a single integer T, denoting the number of test cases. Then the test cases follow.
The first and only line of each test case contains three space-separated integers 
N,A and B respectively — the number of teams, the duration of each round and the length of the breaks between rounds.

"Output Format":-
For each test case, output on a new line the time taken in minutes for the whole event to finish.'''