def fibonacci_generator(n):  # Define the generator function
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


n = int(input())
fib_gen = fibonacci_generator(n)

for fib_number in fib_gen:   # Print the Fibonacci sequence up to the nth term
    print(fib_number)


'''    "Fibonacci Generator":-
Your task is to implement the fibonacci_generator function according to the provided specifications.

"Input Format":-
An integer n (1 <= n <= 100) representing the size of the Fibonacci sequence.

"Output Format":-
Print the Fibonacci sequence up to the nth term on n lines.
'''