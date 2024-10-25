T = int(input())

for i in range(T):
    A,B = map(int,input().split())
    
    X = A //0.1
    Y = B // 0.2
    
    if (X>Y):
        print('FIRST')
        
    elif(X<Y):
        print("SECOND")
        
    else:
        print("ANY")


'''  "Sasta Shark Tank":-

Devendra was offered deals from two investors. The first investor offers A dollars for 10% of his company and the second investor offers B dollars for 20% of his company. Devendra will accept the offer from the investor whose valuation of the company is more. Determine which offer will Devendra accept or if both the offers are equally good.


"Input Format":-
The first line contains a single integer T - the number of test cases. Then the test cases follow.
The first and only line of each test case contains two integers A and B - the amount offered by first investor for 10% of Devendra's company and the amount offered by second investor for 20% of Devendra's company respectively.

"Output Format":-
For each test case, Output FIRST if Devendra should accept the first investor's deal, output SECOND if he should accept the second investor's deal, otherwise output ANY if both deals are equally good.
You may print each character of the strings in uppercase or lowercase (for example, the strings "FiRst", "First", "FIRST", and "FIrst" will all be treated as identical).
'''