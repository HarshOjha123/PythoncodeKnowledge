import numpy as np
array1d=np.array([1,2,3,4])
array2d=np.array([[1,2,3],[4,5,6],[9,96,65]])
array3d=np.array([[[1,2,3],[4,5,6],[7,8,9]],[[11,41,2],[12,3,4],[13,54,12]],[[12,35,66],[45,6,98],[12,98,6]]])
print(array1d)
print(array2d)
print(array3d)

print(array1d[0])
print(array1d[:])
print(array1d[0:])
print(array1d[0:3])
print(array1d[0:3:2])
print(array1d[-1::-1])
print(array1d[0:-2])
#accessing 2d
print(array2d[0][0])
print(array2d[0][-1])
print(array2d[1][0])
print(array2d[2][1])
#slicing 2d
print(array2d[0,0:2])
print(array2d[0:2,0:3])
print(array2d[-3:,-3:])

#acessing 2d
print(array3d[0][1][1])
print(array3d[1][2][0])

#slicing
print(array3d[0:3,0:3,0:3])
print(array3d[1,0:3,0:3])
print(array3d[2,0,0:3])
print(array3d[0,0:3,0])


