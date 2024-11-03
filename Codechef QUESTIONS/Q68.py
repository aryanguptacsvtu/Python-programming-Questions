# cook your dish here
T = int(input())

for i in range(T):
    
    X,Y = map(int, input().split())
    
    if(X<Y):
        print(0)
        
    else:
        print(X//Y)


'''    "Valentine is Coming":-

Valentine's Day is approaching and thus Chef wants to buy some chocolates for someone special.Chef has a total of X rupees and one chocolate costs Y rupees. What is the maximum number of chocolates Chef can buy?


"Input Format":-
First line will contain T, the number of test cases. Then the test cases follow.
Each test case contains a single line of input, two integers X,Y - the amount Chef has and the cost of one chocolate respectively.

"Output Format":-
For each test case, output the maximum number of chocolates Chef can buy.'''