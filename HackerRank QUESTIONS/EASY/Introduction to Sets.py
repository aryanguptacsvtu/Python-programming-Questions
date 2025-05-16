def average(array):
    # your code goes here
    heights = set(array)
    distinct_average = sum(heights) / len(heights)
    return distinct_average


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)


''' "Introduction to Sets":-

"Function Description":-
Complete the average function in the editor below.
'average' has the following parameters:
int arr: an array of integers

"Returns":-
float: the resulting float value rounded to 3 places after the decimal

"Input Format":-
The first line contains the integer,N, the size of arr.
The second line contains the N space-separated integers,arr[i].

"Sample Input":-
10
161 182 161 154 176 170 167 171 170 174

"Sample Output":-
169.375
'''