"""
There is an array of integers. There are also disjoint sets, and , each containing integers. You like all the integers in set and dislike all the integers in set . Your initial happiness is . For each integer in the array, if , you add to your happiness. If , you add

to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since
and

are sets, they have no repeated elements. However, the array might contain duplicate elements.

Constraints


Input Format

The first line contains integers
and separated by a space.
The second line contains integers, the elements of the array.
The third and fourth lines contain integers, and

, respectively.

Output Format

Output a single integer, your total happiness.
"""






size = raw_input()
size = map(int,size.split(' '))
array = raw_input()
array=map(int,array.split(' '))
a2=raw_input()
a2=set(map(int, a2.split(' ')))
a3=raw_input()
a3=set(map(int, a3.split(' ')))

happiness=0
for i in array:
    if(i in a2):
        happiness += 1
    if(i in a3):
        happiness += -1
print(happiness)
