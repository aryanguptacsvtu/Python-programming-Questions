set_a_size = input()  # M
set_a = set(map(int, input().split()))

set_b_size = input()  # N
set_b = set(map(int, input().split()))

symmetric_diff = set_a.symmetric_difference(set_b)

# Print the sorted symmetric difference
for item in sorted(symmetric_diff):
    print(item)


''' "Symmetric Difference":-

"Input Format":-
The first line of input contains an integer, M.
The second line contains M space-separated integers.
The third line contains an integer, N.
The fourth line contains N space-separated integers.

"Output Format":-
Output the symmetric difference integers in ascending order, one per line.

"Sample Input":-
4
2 4 5 9
4
2 4 11 12

"Sample Output":-
5
9
11
12
'''