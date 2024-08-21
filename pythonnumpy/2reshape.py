import numpy as np
array1d=np.array([ x for x in range(1,11)])
print(array1d)
print(array1d.reshape(2,5))#when we reshape then the total no of elemnts present in the given dimension should be equql to the dimension(p*m*n) in which we are changing it.
#print(array1d.reshape(2,2,-1)) it will throw an error as we cannot change 10=(p*n*m)

array2d=np.arange(12)#arange(n)methdod is used to make 1d array of elemnts starting from 0 to n-1
print(array2d)
print(array2d.reshape(3,2,2))
print(array2d.reshape(2,-1))#the program will automatically guess the no at '-1'(unknown dimension) place here it will be 6
print(array2d.reshape(-1,2,3))#here it will be 2
