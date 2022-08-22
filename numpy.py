print('hello world')
import numpy as np

list_1=[1,2,3,4]
array_1=np.array(list_1)
array_1

list_2=[11,22,33,44]
lists=[list_1,list_2]

array_2=np.array(lists)

array_2
array_2.dtype
array_2.shape

my_zeros_array=np.zeros(5)
my_zeros_array.dtype

my_empty_array=np.empty(5)
my_empty_array
my_empty_array.dtype

my_empty_array==my_zeros_array

my_ones_array=np.ones([5,5])
my_ones_array


my_eye_array=np.eye(5)
my_eye_array 

np.arange(5)
np.arange(1,5)
np.arange(1,5,2)

# 
arr1=np.array([[1,2,3,4],[8,9,10,11]])

arr1+arr1
arr1-arr1
arr1*arr1
1/arr1
arr1**3
# 

arr=np.arange(0,11)
arr

arr[8]
arr[0:3]
arr[1:5]
arr[0:5]

arr[0:5]=100
arr

arr=np.arange(0,11)
arr
slice_of_arr=arr[0:5]
slice_of_arr

slice_of_arr[:]=99
slice_of_arr
arr 

arr_copy=arr.copy()


arr_2d=np.array([[5,10,15],[20,25,30],[35,40,45]])
arr_2d
arr_2d[1]
arr_2d[0]
arr_2d[1][0]
arr_2d[:2][1:]

arr2d=np.zeros((10,10))
arr2d
arr2d_length=arr2d.shape()