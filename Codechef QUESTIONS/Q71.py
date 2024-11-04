# cook your dish here
T = int(input())

for i in range(T):
    
    W,X,Y,Z = map(int,input().split())
    
    if(W==X or W==Y or W==Z):
        print("YES")
        
    elif((W==X+Y) or (W==Y+Z) or (W==X+Z)):
        print("YES")
        
    elif(W==X+Y+Z):
        print("YES")
        
    else:
        print("NO")


'''    "Weights":-

Chef is playing with weights. He has an object weighing W units. He also has three weights each of 
X,Y, and Z units respectively. Help him determine whether he can measure the exact weight of the object with one or more of these weights.


"Input Format":-
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of single line containing a four positive integers W,X,Y, and Z.

"Output Format":-
For each test case, output on a new line YES if it is possible to measure the weight of object with one or more of these weights, otherwise print NO.
You may print each character of the string in either uppercase or lowercase (for example, the strings yes, YES, Yes, and yeS will all be treated as identical).'''