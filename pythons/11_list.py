# defining list-we can create list with items of different data types 

l=[1,"harsh",23.4,25,"ojha"]

# slicing is same as string 

# print(l[0]) acessing of values  
 
print(l[:6])
print(l[0:])
print(l[0:6:2])

# change of values at index 

a=[23,"p",76,"lo"]
a[0]=1
a[1]=87
print(a[3],a[0],a[1])

# print(a[10]) out of range error
 
# duplication    
b=a  
print(b)

# methods

l1=[1,20,3,90,5,62,95]
l1.sort()  #use to sort the list
print(l1)
l1.append(4) #is used to add a data at the end of the list 
print(l1)
l1.reverse() # reverse the list
print(l1)
l1.pop(1) #pop the value of given index 
print(l1)
l1.remove(5) #remove value from the list
print(l1)
l1.insert(2,0) #insert at index (index,value) 
print(l1)

c=[10,9,0,8,7,6]
newlist=[x for x in c]
print(newlist)