def name():  #defining function using def keyword
    print("my name is harsh ojha")    
name()    #calling of function

def brothers(name1,name2): #no. of parameters passed during function defining = no of arguments passed otherwise error will arise
    print("big brothers name are",name1,name2)
brothers("ritik","nitesh")    

def father(args1): #parameter passing in function
    print("my father name is",args1)
father("rajesh ojha") #argument passing during function calling

def family_members(*members): # *is used when we dont know the no. of arguments we have to pass is also called arbitrary arguments
   print("my family member has",members[2])
family_members("2brothers","mom an dad","nanig","dadag and dadig")   

def family(brotherss,mother,father): #keyword arguments(key = value) can be passed as a argument
    print("my mother name is" + " " + mother)
family(brotherss="ritik and nitesh",mother="anju ojha",father="rajesh kumar ojha") 

######## ** is used for arbitrary keyword arguments  #######


#default parameter value
def nationality(country="india"):
    print("my country name is",country)
nationality("australia")
nationality("america")
nationality("uk")
nationality("russia")
nationality()   #default parameter value

######## we can pass list as a argument
def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry","mango"]
my_function(fruits) 
    
########  we can use pass statement when we have a empty function to avoid error
    

# using return in function
def kkk(s):
    return 5*s
print(kkk(5)) 
    
#recursion fuction call itself in python it is ristrected upto 1000 times

def recursion():
    print("lol")
    recursion()
recursion()        