t = int(input())

while t > 0:
    x, y, z = map(int, input().split())
    t -= 1
    
    amount = 5*x + 10*y
    
    chocolates = amount//z
    
    print(chocolates)


'''  "Chef and Chocolates":-

Chef has X 5 rupee coins and Y 10 rupee coins. Chef goes to a shop to buy chocolates for Chefina where each chocolate costs Z rupees. Find the maximum number of chocolates that Chef can buy for Chefina.


"Input Format":-
The first line contains a single integer T — the number of test cases. Then the test cases follow.
The first and only line of each test case contains three integers X,Y and Z— the number of 5 rupee coins, the number of 10 rupee coins and the cost of each chocolate.

"Output Format":-
For each test case, output the maximum number of chocolates that Chef can buy for Chefina.'''