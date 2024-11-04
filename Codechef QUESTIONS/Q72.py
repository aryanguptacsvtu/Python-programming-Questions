# cook your dish here
T = int(input())

for i in range(T):
    s,x,y,z=map(int,input().split())
        
    if (x+y+z)<=s:
        print("0")
                
    elif (x+z)<=s or (y+z)<=s:
        print("1")
                
    else:
        print("2")


'''     "Chef and his Apps":-

Chef's phone has a total storage of S MB. Also, Chef has 2 apps already installed on his phone which occupy X MB and Y MB respectively.
He wants to install another app on his phone whose memory requirement is Z MB. For this, he might have to delete the apps already installed on his phone. Determine the minimum number of apps he has to delete from his phone so that he has enough memory to install the third app.


"Input Format":-
The first line contains a single integer T — the number of test cases. Then the test cases follow.
The first and only line of each test case contains four integers S,X,Y and Z — the total memory of Chef's phone, the memory occupied by the two already installed apps and the memory required by the third app.

"Output Format":-
For each test case, output the minimum number of apps Chef has to delete from his phone so that he can install the third app.'''