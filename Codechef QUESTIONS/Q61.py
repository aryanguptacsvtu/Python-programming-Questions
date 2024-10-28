N = int(input())

for i in range(N):
    
    A,B,C = map(int, input().split())
    
    if((A>B and A<C) or (A<B and A>C)):
        print(A)
        
    elif((B>A and B<C) or (B<A and B>C)):
        print(B)
        
    else:
        print(C)


'''   "Second Max of Three Numbers":-
Write a program that accepts sets of three numbers, and prints the second-maximum number among the three.

"Input Format":-
First line contains the number of triples, N.
The next N lines which follow each have three space separated integers.

"Output Format":-
For each of the N triples, output one new line which contains the second-maximum integer among the three.'''