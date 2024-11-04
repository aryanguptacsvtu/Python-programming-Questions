# cook your dish here
T = int(input())

for i in range(T):
    
    n,a,b= map(int,input().split())
    sum=0

    for j in range(1,n+1):
        if j%2==0:
            sum=sum+a 
        else: 
            sum=sum+b

    print(sum)


'''   "Chef Eren":-

Chef is a very big fan of Eren Yeager.In the last season of Attack on Titan, there were N episodes numbered from 1 to N.
Each even indexed episode was A minutes long and each odd indexed episode was B minutes long.
Calculate the total duration (in minutes) of the last season.


"Input Format":-
The first line of input contains a single integer T, the number of test cases.
The first and only line of each test case contains three integers 
N, A, and B, the number of episodes and the durations of each even-indexed and odd-indexed episodes respectively in minutes.

"Output Format":-
For each test case, print a single integer on a new line, the total duration of the last season in minutes.'''