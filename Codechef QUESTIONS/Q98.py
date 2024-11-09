# cook your dish here
T = int(input())

for i in range(T):
    
    A,B,C = map(int, input().split())
    
    cost = (A+B+C) - min(A,B,C)
    
    print(cost)


'''     "Get Lowest Free":-
Chef goes to the supermarket to buy some items. Luckily there's a sale going on under which Chef gets the following offer:
If Chef buys 3 items then he gets the item (out of those 3 items) having the lowest price as free.
Chef buys 3 items having prices A,B and C respectively. What is the amount of money Chef needs to pay?


"Input Format":-
The first line will contain an integer T - number of test cases. Then the test cases follow.
The first and only line of each test case contains three integers A,B,C - the prices of the items bought by Chef.

"Output Format":-
For each test case, output the price paid by Chef.'''