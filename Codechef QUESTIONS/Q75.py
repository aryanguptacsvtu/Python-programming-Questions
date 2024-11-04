# cook your dish here
import math

T = int(input())

for i in range(T):
    
    X,N = map(int, input().split())
    
    total_flights = math.ceil(N/100)
    
    required = total_flights - X
    
    if(total_flights<=X):
        print(0)
        
    else:
        print(required)


'''     "Airlines":-

An airline operates X aircraft every day. Each aircraft can carry up to 100 passengers.
One day, N passengers would like to travel to the same destination. What is the minimum number of new planes that the airline must buy to carry all N passengers?


"Input Format":-
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of a single line containing two space-separated integers X and N — the number of aircraft the airline owns and the number of passengers travelling, respectively.

"Output Format":-
For each test case, output the minimum number of planes the airline needs to purchase.'''