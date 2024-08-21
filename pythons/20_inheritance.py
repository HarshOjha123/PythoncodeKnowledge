#inheritance allows us to copy the functions or attributes of another class
#override hta hai
#can inherit multiple class syntax class child(class1,class2,....classn):
#parent class
class Name():
    def __init__(self,first,last):
        self.first=first
        self.last=last
    def printname(self):    
        print(f"The FIRST name is {self.first} and last name is {self.last}")
f=Name("harsh","ojha")
f.printname()

#child class

class FullName(Name): #pass parent class name as a parameter in chlid class
    pass
g=FullName("rishu","ojha")
g.printname()   

'''When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.'''
  
#To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function

class Student():
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        print(f"the student belongs to csds and are in 3rd year")
    def director(self):
        print("the director is chaturnath lingam") 
class About(Student):
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        Student.__init__(self, fname, lname)  #call of a parent class __init__ function  
    def printName(self):
        print(f"the name of a student is {self.fname} {self.lname}")    
f=About(fname="harsh",lname="ojha")
f.printName() 
f.director()                       
#### Python also has a super() function that will make the child class inherit all the methods and properties from its parent
#syntax super().__init__(fname,lname)
