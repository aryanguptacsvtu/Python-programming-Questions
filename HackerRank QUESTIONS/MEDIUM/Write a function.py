def is_leap(year):
    leap = True
    
    # Write your logic here
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return leap
    else:
        return False

year = int(input())
print(is_leap(year))


''' "Leap Year":-

"Task":-
Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

"Input Format":-
Read 'year', the year to test.

"Output Format":-
The function must return a Boolean value (True/False). Output is handled by the provided code stub.

"Sample Input":-
1990

"Sample Output":-
False
'''