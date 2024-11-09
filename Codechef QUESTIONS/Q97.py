# cook your dish here
T=int(input())

for i in range(T):
    H,X,Y=map(int,input().split())
    a=H-Y

    if(a%X ==0):
        print((a//X)+1)
    else:
        print((a//X)+2)


'''        "Single-use Attack":-

Chef is playing a video game, and is now fighting the final boss.
The boss has H health points. Each attack of Chef reduces the health of the boss by X.
Chef also has a special attack that can be used at most once, and will decrease the health of the boss by Y.
Chef wins when the health of the boss is ≤0.


"Input Format":-
The first line of input will contain a single integer T, denoting the number of test cases.
The first and only line of each test case will contain three space-separated integers H,X,Y — the parameters described in the statement.

"Output Format":-
For each test case, output on a new line the minimum number of attacks needed by Chef to win.
'''