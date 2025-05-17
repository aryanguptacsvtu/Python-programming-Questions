# Enter your code here. Read input from STDIN. Print output to STDOUT
N =int(input())
set1 = set()

for i in range(N):
    set1.add(input())
    
counter = (len(set1))
print(counter)

''' "Set.add()":-

"Input Format":-
The first line contains an integer N, the total number of country stamps.
The next N lines contains the name of the country where the stamp is from.

"Output Format":-
Output the total number of distinct country stamps on a single line.

"Sample Input":-
7
UK
China
USA
France
New Zealand
UK
France 

"Sample Output":-
5
'''