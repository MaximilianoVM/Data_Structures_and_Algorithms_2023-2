from array import * 
import random

def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i 
    return smallest_index

def selection_sort(arr):
    #new_arr = []
    new_arr = array('i', [])
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr

#++++++++++++++++++++++++++++++


# creating an array with integer type
a = array('i', [1, 2, 3, 5, 8, 56, 4, 7, 8, 4, 54, 90, 34, 23, 45, 76, 3, 5, 7, 9, 2, 3,6, 9, 4, 45, 545])

b = array('u', ['max ', 'sean', 'raul', 'valeria', 'samuel', 'norman', 'asael'])

import numpy as np

array1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
array2 = np.array([21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40])
array3 = np.array([41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60])
array4 = np.array([61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80])


###

print('ANTES', a, type(a))

print('=====================')

a_sorted = selection_sort(a)

print('DESPUES',  a_sorted, type(a_sorted))

###
print('\bANTES', b, type(b))

print('=====================')

b_sorted = selection_sort(b)

print('DESPUES',  b_sorted, type(b_sorted))


 