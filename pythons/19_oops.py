#creating class using keyword=class
#Pascal Case=EmployeeName,HarshOjhaName      camelCase= isFloat,isInteger,isHarryGood
#we generally use pascal case for creating classe name and camel case for function
#class doesnt take memory untill the object is intialized
class Student():
    def name(self):#(,nameis)
        nameis="harshojha"
       # self.nameis=nameis
        print(f"The name of a student is {nameis}")#{a.nameis}
a=Student()#object is created
#a.nameis="rishu"
a.name()        

#there are two attributes class and instance attribute
#class attribute is defined with in a class
#instance attribute is defined using object after the class intialization

class Attributes():
    companyname="Google"#class
    location="gurugram"#class
name=Attributes()
name.companyname="youtube"#instance
print(f"the company name is {name.companyname} and located in {name.location}")#if class and instance both is given the instance will have more priority
    
# use of self parameter     

class UseOf():
    def parameter(self):#if we dont use self we get an error during object calling fuction
        print("hello")
harsh=UseOf()
harsh.parameter()# == UseOf.parameter(harsh) we are passing an argument in this calling and if we doesnt define the (self) then it will surely through an error

#static method which alllows us to not pass (self) as a parameter these functions are generally for a mesg
class Static():
    @staticmethod
    def printt():
        print("love coding in python")

c=Static()
c.printt()        

#the __init__() as a constructor runs automatically without any calling
      
class Constructor():
    def __init__(self,name,work,state):
        self.name=name
        self.work=work
        self.state=state
        print(f"The name of the employee is {self.name} have experince in {self.work} work and belong from {self.state}")
l=Constructor("harsh","coding","uttarpradesh")  #we have to pass the arguments here of __init__()
      
#The __str__() function controls what should be returned when the class object is represented as a string.      
#If the __str__() function is not set, the string representation of the object is returned
#without str function same program will <__main__.Person object at 0x1538100cf100>
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  #def __str__(self):
   # return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)

        