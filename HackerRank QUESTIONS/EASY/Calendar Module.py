# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

month, date, year = map(int, input().split())

print((calendar.day_name[calendar.weekday(year, month, date)]).upper())


'''  "Calendar Module":-

"Input Format":-
A single line of input containing the space separated month, day and year, respectively, in MM DD YYYY format.

"Output Format":-
Output the correct day in capital letters.

"Sample Input":-
08 05 2015

"Sample Output":-
WEDNESDAY
'''