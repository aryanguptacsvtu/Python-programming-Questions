T = int(input())

for i in range(T):
    N = int(input())
    
    total_pages=N*1000
    
    notebooks= total_pages//100
    
    print(notebooks)


''' "Count the Notebooks":-

You know that 1 kg of pulp can be used to make 1000 pages and 1 notebook consists of 100 pages.
Suppose a notebook factory receives N kg of pulp, how many notebooks can be made from that?

"Input Format":-
First line will contain T, the number of test cases. Then the test cases follow.
Each test case contains a single integer N - the weight of the pulp the factory has (in kgs).

"Output Format"
For each test case, output the number of notebooks that can be made using N kgs of pulp.'''