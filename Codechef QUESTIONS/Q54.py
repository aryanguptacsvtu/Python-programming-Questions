T = int(input())

for i in range(T):
    
    N = int(input())
    S = input()
    new_str = ''
    
    for i in range(N):
        
        if S[i] == 'A':
            new_str = new_str + "T"

        elif S[i] == 'T':
            new_str = new_str + "A"

        elif S[i] == 'C':
            new_str = new_str + "G"

        elif S[i] == 'G':
            new_str = new_str + "C"
            
    print(new_str)


'''  "Complementary Strand in a DNA":-

You are given the sequence of Nucleotides of one strand of DNA through a string S of length N. S contains the character A,T,C, and G only.
Chef knows that:
A is complementary to T.
T is complementary to A.
C is complementary to G.
G is complementary to C.
Using the string S, determine the sequence of the complementary strand of the DNA.'''
