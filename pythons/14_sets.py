#set is a collection of non repetitive elements
#empty set
s={}     #this wl not be empty set
print (type(s))

i=set()   #empty set
print (type(i))

j={1,2,3,4,"h","a"}
print(j)

#methods
j.add(5)
print(j)
j.add("h") #it will not add again in set because it doesnt allow the repetion of same element

#j.add([2,9,8,7]) it will not add a list in it bacause it is unhashable type(can be changed)
#print(j)

j.add((9,0,8)) #tuple can be added
print(j)

print(len(j)) #length of set
j.remove((9,0,8)) #remove the provided value
print(j)

j.clear() #empty the set
print(j)
print(type(j))

#practice
sets={20,"20",20.0} #all three considerd as a different value(int,str,float) but as 20 and 20.0 is same so it will print only ones a 20
print(sets)
