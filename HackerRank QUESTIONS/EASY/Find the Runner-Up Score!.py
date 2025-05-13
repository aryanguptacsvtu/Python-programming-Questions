if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    scores =list(arr)
    scores.sort(reverse=True)  # Sort list in Descending Order
    highest = scores[0]
    
    runner_up_score = None
    
    for score in scores:
        if score < highest:
            runner_up_score = score
            break
            
    print( runner_up_score)


'''  "Find the Runner-Up Score!":-

"Input Format":-
The first line contains n. The second line contains an array A[] of n integers each separated by a space.

"Output Format":-
Print the runner-up score.

"Sample Input":-
5
2 3 6 6 5

"Sample Output":-
5
'''