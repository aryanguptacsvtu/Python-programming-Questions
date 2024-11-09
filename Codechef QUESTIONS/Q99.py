# cook your dish here
t = int(input())

for i in range(t):
    
    n = int(input())
    a = list(map(int, input().split()))
    
    if (n & 1)==1: 
        print(-1)     # If N is "odd", it's impossible to make  sum 0, so answer is -1.
    
    else: 
        print(abs(sum(a))//2)  # If N is "even", we need to flip half of the sum of array to make it 0.


'''     "Minimum number of Flips":-

Chef has an array A of length N consisting of 1 and -1 only.
In one operation, Chef can choose any index (1≤i≤N) and multiply the element Ai by -1.


"Input Format":-
First line will contain T, number of test cases. Then the test cases follow.
First line of each test case consists of a single integer N denoting the length of the array.
Second line of each test case contains N space-separated integers A1,A2...An denoting the array A.

"Output Format":-
For each test case, output the minimum number of operations to make the sum of the array equal to 0. 
Output -1 if it is not possible to make the sum equal to 0.'''