# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

N = input()
Student = namedtuple('Student',input().split())  
# Reads the column headers (like ID, MARKS, NAME, CLASS) and creates a Student namedtuple

add = 0
for i in range(0,int(N)):
    s = input().split()
    stds = Student(*s)

    add += int(stds.MARKS)
    
    
print("{:.2f}".format(add/int(N)))


''' "Collections.namedtuple()":-

"Input Format":-
The first line contains an integer N, the total number of students.
The second line contains the names of the columns in any order.
The next N lines contains the marks,IDs, name and class, under their respective column names.

"Output Format":-
Print the average marks of the list corrected to 2 decimal places.

"Sample Input":-
5
ID         MARKS      NAME       CLASS
1          97         Raymond    7
2          50         Steven     4
3          91         Adrian     9
4          72         Stewart    5
5          80         Peter      6

"Sample Output":-
78.00
'''