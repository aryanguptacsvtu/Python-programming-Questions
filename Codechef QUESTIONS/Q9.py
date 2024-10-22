t = int(input())
for i in range(t):
    X, Y = map(int, input().split())

    prize_top10 = 10*X           
    prize_11to100 = 90*Y  
           
    print(prize_top10+prize_11to100) 


'''"Total prize money":-

In a coding contest, there are prizes for the top rankers. The prize scheme is as follows:

Top 10 participants receive rupees X each.
Participants with rank 11 to 100(both inclusive) receive rupees Y each.
Find the total prize money over all the participants.

"Input Format":-
First line will contain T, number of test cases. Then the test cases follow.
Each test case contains of a single line of input, two integers X and Y - the prize for top 10 rankers and the prize for ranks 11 to 100 respectively.
'''