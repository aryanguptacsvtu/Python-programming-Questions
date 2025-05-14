if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    t = tuple(integer_list)
    print(hash(t))


'''  "Tuples":-

"Input Format":-
The first line contains an integer ,n, denoting the number of elements in the tuple .
The second line contains n space-separated integers describing the elements in tuple t.

"Output Format":-
Print the result of hash(t).

"Sample Input":-
2
1 2

"Sample Output":-
3713081631934410656
'''