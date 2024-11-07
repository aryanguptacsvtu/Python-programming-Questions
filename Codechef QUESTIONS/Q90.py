# cook your dish here
T = int(input())

for i in range(T):
    N = int(input())
    
    print(N - (N//5))


'''   "Presents for Cheffina":-

Chef has fallen in love with Cheffina, and wants to buy N gifts for her. On reaching the gift shop, Chef got to know the following two things:
The cost of each gift is 1 coin.
On the purchase of every 4th gift, Chef gets the 5th gift free of cost.


"Input Format":-
The first line of input will contain an integer T — the number of test cases. The description of T test cases follows.
The first and only line of each test case contains an integer N, the number of gifts in the shop.

"Output Format":-
For each test case, output on a new line the minimum number of coins that Chef will require to obtain all N gifts.'''