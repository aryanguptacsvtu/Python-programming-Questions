# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
A = map(int, input().split())
B = map(int, input().split())

cartesian_product = list(product(A, B))

for pair in cartesian_product:
    print(pair, end = ' ')


'''  "itertools.product()":-

"Task":-
You are given a two lists A and B. Your task is to compute their cartesian product AXB.

"Input Format":-
The first line contains the space separated elements of list A.
The second line contains the space separated elements of list B.
Both lists have no duplicate integer elements.

"Output Format":-
Output the space separated tuples of the cartesian product.

"Sample Input":-
1 2
3 4

"Sample Output":-
(1, 3) (1, 4) (2, 3) (2, 4)
'''