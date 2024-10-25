T = int(input())

for i in range(T):
    N = int(input())
    
    if(N%4==0):
        print("Good")
        
    else:
        print("Not Good")


'''  "Good Program":-

In computing, the collection of four bits is called a nibble.
Chef defines a program as:
Good, if it takes exactly X nibbles of memory, where X is a positive integer.Not Good, otherwise.
Given a program which takes N bits of memory, determine whether it is Good or Not Good.


"Input Format":-
First line will contain T, number of test cases. Then the test cases follow.
The first and only line of each test case contains a single integer N, the number of bits taken by the program.

"Output Format":-
For each test case, output Good or Not Good in a single line. You may print each character of Good or Not Good in uppercase or lowercase (for example, GoOd,GOOD,good will be considered identical).'''