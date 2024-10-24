T = int(input())

for i in range(T):
    N = int(input())
    
    l = list(map(int,input().split()))
    count =0
    
    for item in l:
        if(item>=1000):
            count = count+1

    print(count)


'''   "Problems in your to-do list":-

Chef is a beginner and should ideally try and solve only problems with difficulty rating strictly less than 1000. Given a list of difficulty ratings for problems in the Chef's to-do list, please help him identify how many of those problems Chef should remove from his to-do list, so that he is only left with problems of difficulty rating less than 1000.


"Input Format":-
The first line of input will contain a single integer T, the number of test cases. Then the testcases follow.
Each testcase consists of 2 lines of input.
The first line of input of each test case contains a single integer, N, which is the total number of problems that the Chef has added to his to-do list.
The second line of input of each test case contains N space-separated integers D1,D2...Dn , which are the difficulty ratings for each problem in the to-do list.

"Output Format":-
For each test case, output in a single line the number of problems that Chef will have to remove so that all remaining problems have a difficulty rating strictly less than 1000.
'''