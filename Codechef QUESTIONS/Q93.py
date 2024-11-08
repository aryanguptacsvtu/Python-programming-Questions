# cook your dish here
R , O , C = map(int, input().split())

remaining_overs = 20-O 
max_runs = 6*remaining_overs*6

total = C + max_runs

if(total > R):
    print("YES")
    
else:
    print("NO")


'''      "Possible Victory":-

Chef is playing in a T20 cricket match. In a match, Team A plays for 20 overs. In a single over, the team gets to play 6 times, and in each of these 6 tries, they can score a maximum of 6 runs. After Team A's 20 overs are finished, Team B similarly plays for 20 overs and tries to get a higher total score than the first team. The team with the higher total score at the end wins the match.
Chef is in Team B. Team A has already played their 20 overs, and have gotten a score of R. Chef's Team B has started playing, and have already scored C runs in the first O overs. In the remaining 
20-O overs, find whether it is possible for Chef's Team B to get a score high enough to win the game. That is, can their final score be strictly larger than R?


"Input Format":-
There is a single line of input, with three integers, R,O,C.

"Output Format":-
Output in a single line, the answer, which should be "YES" if it's possible for Chef's Team B to win the match and "NO" if not.'''