# cook your dish here
T = int(input())

for i in range(T):
    A, B ,C = map(int, input().split())
    
    if((A>B and A<C) or (A<B and A>C)):
        print(A)
        
    elif((B>A and B<C) or (B<A and B>C)):
        print(B)
        
    else:
        print(C)


'''    "Second Largest":-
Three numbers A, B and C are the inputs. Write a program to find second largest among them.


"Input Format":-
The first line contains an integer T, the total number of testcases. Then T lines follow, each line contains three integers A, B and C.

"Output Format":-
For each test case, display the second largest among A, B and C, in a new line.
'''