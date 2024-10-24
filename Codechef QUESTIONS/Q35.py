T = int(input())

for i in range(T):
    N = int(input())
    reversedNum=0
    
    while(N!=0):
        remainder = N%10
        reversedNum = reversedNum*10 + remainder
        N= N//10
        
    print(reversedNum)


'''  "Reverse The Number":-
Given an Integer N, write a program to reverse it.

"Input":-
The first line contains an integer T, total number of testcases.Then follow T lines,each line contains an integer N.

"Output":-
For each test case, display the reverse of the given number N, in a new line.'''