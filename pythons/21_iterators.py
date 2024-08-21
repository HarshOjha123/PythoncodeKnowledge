list1=["and","how","long","short"]#LIST ,TUPLES ,DICT,SETS ALL ARE ITERABLE OBJECTS
T1=("char","int","boolean")
S1={"lamda","string","operators"}
D1={
    "gun":{"vandal":"singleshot",
        "phantom":"auto",
        "operator":"sniper",}
}                   
#iter()and next() are two functions for iteration
myiter=iter(list1)
print(next(myiter))
print(next(myiter))
print(next(myiter))

#iteration with for loop
for i in T1:
    print(i)
#iteratrion through string
s="harsh"
for i in s:
    print(i)
# for stoping iteration we use stopiteration statement with if else syntax ''' raise stopiteration'''
               

