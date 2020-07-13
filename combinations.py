'''
This tool returns the

length subsequences of elements from the input iterable.

Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.


Task

You are given a string
.
Your task is to print all possible combinations, up to size

, of the string in lexicographic sorted order.

Input Format

A single line containing the string
and integer value

separated by a space.

Constraints


The string contains only UPPERCASE characters.

Output Format

Print the different combinations of string
on separate lines.

'''


from itertools import permutations, product, combinations
A = map(str,raw_input().split(' '))
word, length = A[:]
word=sorted(word)
for r in range(1,int(length)+1):
    l = list(combinations(word,r))
    for i in l:
             print(''.join(i[z] for z in range(len(i))))
