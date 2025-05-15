def count_substring(string, sub_string):
    count=0

    for c in range(len(string)):
        for s in range(len(sub_string)):
            
            if c == len(string):
                break
            if string[c] != sub_string[s]:
                break
            elif s == len(sub_string)-1:
                count += 1
                c -= 1
            else:
                c +=1

    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)


''' "Find a String":-

"Input Format":-
The first line of input contains the original string. The next line contains the substring.

"Output Format":-
Output the integer number indicating the total number of occurrences of the substring in the original string.

"Sample Input":-
ABCDCDC
CDC

"Sample Output":-
2
'''