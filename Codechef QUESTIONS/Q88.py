# cook your dish here
T = int(input())

for i in range(T):
    
    X,Y,A,B = map(int, input().split())
    
    if((X==A or X==B) and (Y==A or Y==B)):
        print(0)
        
    elif(X==A or X==B):
        print(1)
        
    elif(Y==A or Y==B):
        print(1)
    
    else:
        print(2)


'''      "Chef and Races":-

The National Championships are starting soon. There are 4 race categories, numbered from 1 to 4, that Chef is interested in. Chef is participating in exactly 2 of these categories.
Chef has an arch-rival who is, unfortunately, the only person participating who is better than Chef, i.e, Chef can't defeat the arch-rival in any of the four race categories but can defeat anyone else. Chef's arch-rival is also participating in exactly 2 of the four categories.
Chef hopes to not fall into the same categories as that of the arch-rival.


"Input Format":-
The first line of input contains an integer T, denoting the number of testcases. The description of T testcases follows.
Each testcase consists of a single line containing four space-separated integers — the values of X,Y,A, and B respectively.

"Output Format":-
For each testcase, print a single line containing one integer — the maximum number of gold medals that Chef can win.'''