# cook your dish here
T = int(input())

for i in range(T):
    A,B = map(int, input().split())
     
    if(A<B):
        print("<")
        
    elif(A>B):
        print(">")
        
    else:
        print("=")


'''     "Chef And Operators":-

Chef has just started Programming, he is in first year of Engineering. Chef is reading about Relational Operators.
Relational Operators are operators which check relationship between two values. Given two numerical values A and B you need to help chef in finding the relationship between them.


"Input Format":-
First line contains an integer T, which denotes the number of testcases. Each of the T lines contain two integers A and B.

"Output Format":-
For each line of input produce one line of output. This line contains any one of the relational operators
'<' , '>' , '='. '''