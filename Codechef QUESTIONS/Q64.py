T = int(input())

for i in range(T):
    
    N = int(input())
    remainder =0
    sum =0
    
    while(N!=0):
    
        remainder = N % 10
        N = N //10
        sum = sum + remainder
        
    print(sum)


'''
"Sum of Digits":-
You're given an integer N. Write a program to calculate the sum of all the digits of N.

"Input Format":-
The first line contains an integer T, the total number of testcases. Then follow T lines, each line contains an integer N.

"Output Format":-
For each test case, calculate the sum of digits of N, and display it in a new line.'''