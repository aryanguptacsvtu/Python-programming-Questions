# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    # Write your code here
    print(f'Hello {first} {last}! You just delved into python.')

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


''' "What's Your Name?":-

"Input Format":-
The first line contains the first name, and the second line contains the last name.

"Sample Input":-
Ross
Taylor

"Sample Output":-
Hello Ross Taylor! You just delved into python.
'''