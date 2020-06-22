"""
Task
Given sets of integers, and , print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either or

but do not exist in both.

Input Format

The first line of input contains an integer,
.
The second line contains space-separated integers.
The third line contains an integer, .
The fourth line contains

space-separated integers.

Output Format

Output the symmetric difference integers in ascending order, one per line.
"""

n=int(raw_input())
b=raw_input()
z=int(raw_input())
d=raw_input()
l1=map(int, b.split(' '))
l2=map(int, d.split(' '))
s1=set(l1)
s2=set(l2)
s3=s1.symmetric_difference(s2)
for i in range(len(s3)):
    print(min(s3)); s3.discard(min(s3)) 
