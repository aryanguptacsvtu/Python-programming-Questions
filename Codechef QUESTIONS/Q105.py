T = int(input())

for i in range(T):
    N = int(input())

    if (N <= 1):
        print("no")
        
    else:
        is_prime = True
        i=2
        
        while (i <= N / 2):
            
            if (N % i == 0):
                is_prime = False
                break

            i = i+1
        
        if (is_prime):
            print("yes")
        else:
            print("no")


'''        "Primality Test":-

Alice says out an integer and Bob has to say whether the number is prime or not. Bob as usual knows the logic but since Alice doesn't give Bob much time to think, so Bob decides to write a computer program.
Help Bob accomplish this task by writing a computer program which will calculate whether the number is prime or not.Note that 1 is not a prime number.


"Input Format":-
The first line of the input contains an integer T, the number of testcases. T lines follow.
Each of the next T lines contains an integer N which has to be tested for primality.

"Output Format":-
For each test case output in a separate line, "yes" if the number is prime else "no."'''