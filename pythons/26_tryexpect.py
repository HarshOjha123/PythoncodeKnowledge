#excetion handling
#try block is used for testing a block of code 
'''try:
    x=10
    print(x+y)
except:
    print("expect is executed")
'''
'''try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")'''
  
#else command is executed if there is no error or exception

'''try:
    print("hello")
except:
    print("error occured")
else:
    print("no error")'''

#finally command is excuted either error occur or not

try:
    print(x)
except:
    print("error occured")
else:
    print("error not occured")
finally:
    print("i will excute always")

#To throw (or raise) an exception, use the raise keyword.

'''x=0
if x<1:
    raise Exception("no no.s allowed below 1")'''

y=-28
if y<0:
    raise TypeError("no should not be less than 0")