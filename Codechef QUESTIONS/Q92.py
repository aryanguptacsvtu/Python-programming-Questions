T = int(input())

for _ in range(T):
    N = int(input())
    
    if N < 2:
        print(0)

    else:
        complete_weeks = N // 7
        leftover_days = N % 7
        
        # Total Tuesdays is one per week + 1 if leftover_days contains a Tuesday
        tuesdays = complete_weeks + (1 if leftover_days >= 2 else 0)  
        
        print(tuesdays)


'''      "Dracula Eats":-

There are N spooky days left until Halloween.Dracula dines at a mysterious restaurant that changes its spooky menu daily. He particularly enjoys what they serve on Tuesday.
Today is Monday, so he wishes to calculate how many times he can indulge in his favourite menu in the next N days (including today) before Halloween.
Note that Dracula follows the standard 7-day calendar, with Tuesday immediately following Monday.


"Input Format":-
The first line of input will contain a single integer T, denoting the number of test cases.
The only line of each test case contains a single integer N, denoting the number of spooky days.

"Output Format":-
For each test case, output on a new line the number of times Dracula would have had his favorite meal after N days.
'''