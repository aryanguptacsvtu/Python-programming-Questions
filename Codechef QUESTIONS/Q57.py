import math

T = int(input())

for i in range(T):
    
    N = int(input())
    
    print(math.floor(math.sqrt(N)))


'''   "Finding Square Roots":-

In olden days finding square roots seemed to be difficult but nowadays it can be easily done using in-built functions available across many languages .Assume that you happen to hear the above words and you want to give a try in finding the square root of any given integer using in-built functions.


"Input Format":-
The first line of the input contains an integer T, the number of test cases. T lines follow. Each line contains an integer N whose square root needs to be computed.

"Output Format":-
For each line of the input, output the square root of the input integer, rounded down to the nearest integer, in a new line.'''