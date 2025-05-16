# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())

for i in range(T):
    a, b = input().split() 

    try:
        result = int(a)//int(b)

    except ZeroDivisionError as e:
        print(f"Error Code:",e)

    except ValueError as e:
        print(f"Error Code:",e)   

    else:
        print(result)


''' "Exceptions":-

"Input Format":-
The first line contains T , the number of test cases.
The next T lines each contain the space separated values of a and b.

Output Format:-
Print the value of a/b .
In the case of ZeroDivisionError or ValueError, print the error code.

"Sample Input":-
3
1 0
2 $
3 1

"Sample Output":-
Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'
3
'''