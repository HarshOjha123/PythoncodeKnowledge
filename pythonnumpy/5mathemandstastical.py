import numpy as np
x=np.array([x for x in range(1,11)])
print(np.max(x))
y=x.reshape(2,5)
print(y)
print(np.amax(y,axis=0))#axis=0 means in vertical max elements , axis=1 means in horizontal max elements
print(np.amax(y,axis=1))
print(np.amin(y,axis=0))
print(np.amin(y,axis=1))
print(np.median(y))
print(np.mean(y))
print(np.std(y))
print(np.var(y))
print(np.percentile(y,10))
deg=np.array([0,30,45,60,75,90])#degree into radiance
print(np.sin(deg*np.pi/180))
print(np.cos(deg*np.pi/180))
print(np.tan(deg*np.pi/180))