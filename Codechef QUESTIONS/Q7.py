t = int(input())
for i in range(0,t):
    x,y = map(int,input().split())

    if (x+y >6):
        print("YES")
    else:
        print("NO")

'''Good Turn
Chef and Chefina are playing with dice. In one turn, both of them roll their dice at once.

They consider a turn to be good if the sum of the numbers on their dice is greater than 6.
Given that in a particular turn Chef and Chefina got X and Y on their respective dice, find whether the turn was good.
For each test case, output on a new line, YES, if the turn was good and NO otherwise.'''