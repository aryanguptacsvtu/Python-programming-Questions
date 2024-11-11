# cook your dish here
T = int(input())

for i in range(T):
    
    N = int(input())
    a = list( input().split())
    
    count1=0
    count2=0
    
    for item in a:
        
        if (item=="START38"):
            count1 = count1 +1
            
        else:
            count2 = count2 +1
            
    print(count1 ,count2 )


'''    "Recent contest problems":-

Chef has been participating regularly in rated contests but missed the last two contests due to his college exams. He now wants to solve them and so he visits the practice page to view these problems.
Given a list of N contest codes, where each contest code is either START38 or LTIME108, help Chef count how many problems were featured in each of the contests.


"Input Format":-
First line will contain T, number of test cases. Then the test cases follow.
Each test case contains of two lines of input.
First line of input contains the total count of problems that appeared in the two recent contests - N.
Second line of input contains the list of N contest codes. Each code is either START38 or LTIME108, to which each problem belongs.

"Output Format":-
For each test case, output two integers in a single new line - the first integer should be the number of problems in START38, and the second integer should be the number of problems in LTIME108.
'''