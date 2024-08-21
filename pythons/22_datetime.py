import datetime
x=datetime.datetime.now()
print(x)

'''The method is called strftime(), and takes one parameter, format, to specify the format of the returned string'''

print(x.strftime("%A"))

