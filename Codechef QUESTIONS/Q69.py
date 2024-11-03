# cook your dish here
T = int(input())

for i in range(T):
    
    P,Q = map(int, input().split())
    
    if((P+Q)% 4==0 or (P+Q)% 4==1):
        print("Alice")
        
    else:
        print("Bob")


'''    "It is My Serve":-

Alice and Bob are playing a game of table tennis where irrespective of the point scored, every player makes 2 consecutive serves before the service changes. Alice makes the first serve of the match. Therefore the first 2 serves will be made by Alice, then the next 2 serves will be made by Bob and so on.
After the score reaches P and Q for Alice and Bob respectively, both the players forgot whose serve it is. Help them determine whose service it is.


"Input Format":-
The first line contains a single integer T — the number of test cases. Then the test cases follow.
The first line of each test case contains two integers P and Q — the score of Alice and Bob respectively.

"Output Format":-
For each test case, determine which player's (Alice or Bob) serve it is.
You may print each character of Alice and Bob in uppercase or lowercase (for example, Bob, BOB, boB will be considered identical).'''