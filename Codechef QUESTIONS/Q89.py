# cook your dish here
import math
T = int(input())

for i in range(T):
    
    X,Y,R = map(int, input().split())
    
    extra_sticks = R // 30
    total_sticks = X + extra_sticks 
    
    print(math.ceil(total_sticks / Y))


'''    "Endless Appetizers":-

Chef's colleague issued a challenge to Chef: "If you eat more than X mozzarella sticks, I'll give you 30 rupees for each extra one you eat".
Note:
Chef won't order a new plate till he finishes eating all the sticks from the previous one.
However, it's possible that Chef didn't finish all the sticks from the final plate he ordered.
See the explained examples below for more clarification.


"Input Format":-
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of one line of input, containing three space-separated integers X,Y, and R — the lower limit on the number of sticks, the number of sticks on a single plate, and the money received by Chef.

"Output Format":-
For each test case, output on a new line the answer: the maximum number of plates Chef could have ordered.'''