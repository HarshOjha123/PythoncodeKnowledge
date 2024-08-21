#lambda function
x=lambda a,b,c:a*b+c #syntax   lambda parameters:expression
print(x(5,8,9))

#lambda function as a anonymous function
def avg(n):
    return lambda x,y:(x+y)/n
value=avg(2)
print(value(6,8))

#example
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

