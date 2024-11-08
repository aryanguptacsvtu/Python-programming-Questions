# cook your dish here
T = int(input())
 
for i in range(T):
     
    N,K = map(int, input().split())
    l = list(map(int, input().split()))
    
    count = 0
    
    for item in l:

        if((item+K) % 7==0):
            count = count+1
            
    print(count)


'''     "Mutated Minions":-

Each minion has an intrinsic characteristic value (similar to our DNA), which is an integer. The transmogrifier adds an integer K to each of the minions' characteristic value.
Gru knows that if the new characteristic value of a minion is divisible by 7, then it will have Wolverine-like mutations.
Given the initial characteristic integers of N minions, all of which are then transmogrified, find out how many of them become Wolverine-like.


"Input Format":-
The first line contains one integer, T, which is the number of test cases.
Each test case contains of 2 lines of input.
The first line contains two integers N and K, as described in the statement.
The next line contains N integers, which denote the initial characteristic values for the minions.

"Output Format":-
For each testcase, output one integer in a new line, which is the number of Wolverine-like minions after the transmogrification.'''