'''
Given a 2D Array
We define an hourglass in to be a subset of values with indices falling.
There are hourglasses in , and an hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in,
then print the maximum hourglass sum.
Function Description

Complete the function hourglassSum in the editor below. It should return an integer, the maximum hourglass sum in the array.

hourglassSum has the following parameter(s):

arr: an array of integers

Output Format

Print the largest (maximum) hourglass sum found in arr.

'''



import numpy as np
# this function only work on 6X6 2d array
def sum_2darray(arr):
    if(type(arr)!='numpy.ndarray'):
        a=np.asarray(arr)
    else:
        a=arr
    end_row = 3
    l = []
    for i in range(6):
        end_column = 3
        for j in range(6): # the nested for loop creates only 3X3 2D array
            d=np.array(a[i:end_row,j:end_column]) 
            end_column += 1
            if(d.shape == (3L,3L)):
                d[1,0] = 0
                d[1,2] = 0
                l.append(np.sum(d))
            else:
                continue
    end_row += 1
    return(max(l))
