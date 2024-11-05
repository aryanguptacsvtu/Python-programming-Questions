# cook your dish here
T = int(input())

for i in range(T):
    
    A,X,B,Y = map(int, input().split())
    
    speed_Alice = A/X
    speed_Bob = B/Y
    
    if(speed_Alice > speed_Bob):
        print("Alice")
        
    elif (speed_Alice < speed_Bob):
        print("Bob")
        
    else:
        print("Equal")
    

'''     "Speed Limit Test":-

Alice is driving from her home to her office which is A kilometers away and will take her X hours to reach.
Bob is driving from his home to his office which is B kilometers away and will take him Y hours to reach.
Determine who is driving faster, else, if they are both driving at the same speed print EQUAL.


"Input Format":-
The first line will contain T, the number of test cases. Then the test cases follow.
Each test case consists of a single line of input, containing four integers A,X,B, and Y, the distances and and the times taken by Alice and Bob respectively.

"Output Format":-
For each test case, if Alice is faster, print ALICE. Else if Bob is faster, print BOB. If both are equal, print EQUAL.
You may print each character of the string in uppercase or lowercase (for example, the strings equal, equAL, EquAl, and EQUAL will all be treated as identical).'''