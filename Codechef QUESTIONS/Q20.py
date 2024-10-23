T = int(input())

for i in range(T):
    
    X = int(input())
    
    if(X<=100):
        print(X)
        
    elif(X>100 and X<=1000):
        print(X-25)
        
    elif(X>1000 and X<=5000):
        print(X-100)
        
    else:
        print(X-500)


''' "Sale Season":-

It's the sale season again and Chef bought items worth a total of X rupees. The sale season offer is as follows:
if X≤100, no discount.
if 100<X≤1000, discount is 25 rupees.
if 1000<X≤5000,  discount is 100 rupees.
if X>5000,  discount is 500 rupees.
Find the final amount Chef needs to pay for his shopping.

"Input Format":-
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of single line of input containing an integer X.

"Output Format":-
For each test case, output on a new line the final amount Chef needs to pay for his shopping.'''