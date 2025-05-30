import textwrap

def wrap(string, max_width):
    return textwrap.fill(string,max_width) 

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


''' "Text Wrap":-

"Function Description":-
Complete the wrap function in the editor below.
wrap has the following parameters:
string string: a long string
int max_width: the width to wrap to

"Returns":-
string: a single string with newline characters ('\n') where the breaks should be

"Input Format":-
The first line contains a string,'string'.
The second line contains the width, 'max_width'.

"Sample Input":-
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

"Sample Output":-
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
'''