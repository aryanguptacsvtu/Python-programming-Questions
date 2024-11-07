# cook your dish here
T = int(input())

for i in range(T):
    N = int(input())
    
    print(N*(N-1))


'''    "Chef Fantasy 11":-

For a certain cricket match, Chef has decided upon his team of 11 players. However, he hasn't yet decided who should be the captain and who should be the vice-captain.
He's narrowed his decision down to N players out of the 11, from which he'll choose one to be the captain and one to be the vice captain.How many different choices does he have?


"Input Format":-
The first line of input will contain a single integer T, denoting the number of test cases.
The first and the only line of each testcase contains a single integer N, the number of players Chef is considering.

"Output Format":-
For each test case, output on a new line the number of possible choices of captain and vice-captain.'''