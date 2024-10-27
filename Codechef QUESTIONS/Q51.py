T=int(input())

for i in range(T):
    X=int(input())
    
    if (X % 3==1):
        print("HUGE")
        
    elif (X % 3==2):
        print("SMALL")
        
    else:
        print("NORMAL")


'''   "Mario and Transformation":-

Mario transforms each time he eats a mushroom as follows:
If he is currently small, he turns normal.
If he is currently normal, he turns huge.
If he is currently huge, he turns small.
Given that Mario was initially normal, find his size after eating X mushrooms.


"Input Format":-
The first line of input will contain one integer T, the number of test cases. Then the test cases follow.
Each test case contains a single line of input, containing one integer X.

"Output Format":-
For each test case, output in a single line Mario's size after eating X mushrooms.'''