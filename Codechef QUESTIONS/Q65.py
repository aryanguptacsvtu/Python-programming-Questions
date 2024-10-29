t = int(input())

while t > 0:
    a = int(input())
    t -= 1
    
    if(a%2==0 and a%7==0):
        print('Alice')
        
    elif(a%2!=0 and a%9==0):
        print('Bob')
        
    else:
        print('Charlie')


'''   "Favourite Numbers":-

Alice likes numbers which are even, and are a multiple of 7.
Bob likes numbers which are odd, and are a multiple of 9.
Alice, Bob, and Charlie find a number A.
If Alice likes A, Alice takes home the number.
If Bob likes A, Bob takes home the number.
If both Alice and Bob don't like the number, Charlie takes it home.
Given A, find who takes it home.


"Input Format":-
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of a single integer, A.

"Output Format":-
For each test case, output on a new line who takes the number home - "Alice", "Bob", or "Charlie".
You may print each character in uppercase or lowercase. For example, Alice, alice, aLiCe, and ALICE are all considered identical.'''