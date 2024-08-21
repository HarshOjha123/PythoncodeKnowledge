# creating dictionbary= collection pf key and value pairs
mydictionary={} #empty dict

print(type(mydictionary))
mydict={
    "name":"harsh",
    1:3,
    "rollno":2002901540041,
    "marks":[1,2,3,4,5], #defining list in dict
    "NAME":{"SURNAME":"OJHA"}, #defining (key,value) inside a key
    "SUB":(2,3,4,8) #defining tuple in dict
}
print(mydict)
print(mydict[1])
print(mydict['NAME']["SURNAME"])

#OVERRIDING
mydict['rollno']=[2002901540042] #overriding value
print(mydict["rollno"])
mydict={                 #overriding dictionary
    "name":"ayush"
}
print(mydict["name"])
print(mydict)

#methods

mydict={
    "name":"harsh",
    1:3,
    "rollno":2002901540041,
    "marks":[1,2,3,4,5], #defining list in dict
    "NAME":{"SURNAME":"OJHA"}, #defining (key,value) inside a key
    "SUB":(2,3,4,8) #defining tuple in dict
}
print(mydict.keys())
print(mydict.values())
print(mydict.get("name")) #if the key is not present in the dict. then it will return none will not give error
print(mydict.items()) #print dict (key,value) in tuple

#adding a(key,value) pair in a dictionary using update function
r={
    "i":23
}
mydict.update(r)
print(mydict)
 