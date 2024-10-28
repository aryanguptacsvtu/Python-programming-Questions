T = int(input())

for _ in range(T):

    N, K, M = map(int, input().split())
    
    bag_capacity = K * M     # Capacity of one bag
    
    bags_needed = (N + bag_capacity - 1) // bag_capacity    # Minimum number of bags needed
    
    print(bags_needed)


'''   "Fill Candies":-

Chef received N candies on his birthday. He wants to put these candies in some bags. A bag has K pockets and each pocket can hold at most M candies. Find the minimum number of bags Chef needs so that he can put every candy into a bag.


"Input Format":-
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of a single line containing three space-separated integers N,K,M.

"Output Format":-
For each test case, print the minimum number of bags Chef needs so that he can put all the candies in one of the bags.'''