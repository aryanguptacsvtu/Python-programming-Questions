# cook your dish here
T = int(input())

for i in range(T):
    
    X1,Y1,X2,Y2 = map(int, input().split())
    
    first = abs(X1-X2)
    second = abs(Y1-Y2)
    
    print(max(first,second))


'''   "Chessboard Distance":-

The Chessboard Distance for any two points (X1,Y1) and (X2, Y2) on a Cartesian plane is defined as max(|X1-X2| ,|Y1-Y2|)  
You are given two points (X1,Y1) , (X2,Y2). Output their Chessboard Distance.


"Input Format":-
First line will contain T, the number of test cases. Then the test cases follow.
Each test case consists of a single line of input containing 4 space separated integers - X1,Y1,X2,Y2 - as defined in the problem statement.

"Output Format":-
For each test case, output in a single line the chessboard distance between (X1, Y1) and (X2, Y2).
'''