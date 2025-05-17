# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
ab = int(input())
bc = int(input())

print(str(round( math.degrees(math.atan(ab/bc)) ))+'\xb0')


''' "Find Angle MBC":-

Input Format:-
The first line contains the length of side AB.
The second line contains the length of side BC.

"Output Format":-
Output angle MBC in degrees.
Note Round the angle to the nearest integer.

"Sample Input":-
10
10

"Sample Output":-
45°
'''