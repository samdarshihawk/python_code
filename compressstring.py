'''
In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools . To read more about this function, Check this out .

You are given a string
Suppose a character '' occurs consecutively times in the string. Replace these consecutive occurrences of the character in the string.


Input Format

A single line of input consisting of the string


Output Format

A single line of output consisting of the modified string.
'''


from itertools import groupby
a = map(str, raw_input().rstrip())
key_func = lambda x: x[0:]
l=[]
z=[]
for key, group in groupby(a, key_func):
    l.append(key)
    z.append(len(list(group)))

print(' '.join(('('+str(i)+', '+str(j)+')') for i,j in zip(z, l)))
