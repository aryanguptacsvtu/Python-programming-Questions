import math

T = int(input())

for i in range(T):
    
    N = int(input())
        
    required = math.ceil(N/4)
    print(required)


'''  "Minimum Cars required":-

A single car can accommodate at most 4 people.N friends want to go to a restaurant for a party. Find the minimum number of cars required to accommodate all the friends.


"Input Format":-
The first line contains a single integer T - the number of test cases. Then the test cases follow.
The first and only line of each test case contains an integer N - denoting the number of friends.

"Output Format":-
For each test case, output the minimum number of cars required to accommodate all the friends.'''