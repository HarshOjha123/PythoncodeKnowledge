import numpy as np
array0d=np.array(0)
array1d=np.array([1,2,3,45,6])
array2d=np.array([[1,2,3,4],[5,6,7,8],[10,11,12,13]])
array3d=np.array([[[1,2,3],
                   [3,4,5],
                   [5,9,7]],
                  [[23,7,8],
                   [25,9,65],
                   [2,98,35]],
                  [[138,68,5],
                   [36,98,64],
                   [2,6,6]]])
print(len(array3d[0]))
print(len(array3d))
print(array0d.ndim) #ndim is used to find the dimension of ndarray
print(array1d.ndim)
print(array2d.ndim)
print(array3d.ndim)

print(array0d.shape)#shape is used to find out the no.of pages,rows and coloumnsn of nd array 
print(array1d.shape)
print(array2d.shape)
print(array3d.shape)

print(array0d.size)# size tells the total no.of elements present in the ndarray
print(array1d.size)
print(array2d.size)
print(array3d.size)

print(type(array2d))#class numoy.ndarray

print(array0d.dtype)#numpy provides type of his own ex int-64,int-32,float-64 and etc
print(array2d.itemsize)#size of each elements in bits of nd array int32= 32/8=4,float-64=64/8=8
print(array3d.data)#starting location of storage of array in memory
  