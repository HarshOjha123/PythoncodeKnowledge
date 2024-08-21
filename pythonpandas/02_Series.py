#A Pandas Series is like a column in a table.It is a one-dimensional array holding data of any type.

import pandas as pd
cars=["mustang","rollsroyce","bmw"]
y=pd.Series(cars)
print(y)
#in the given o/p 0,1,2 are labels assigned automatically 

classroom={"harsh" :2002901540041,
           "dev":2002901540032,
           "istekhar":2002901540048}
x=pd.Series(classroom)
z=x[0]
print(x)
print(z)

#in this example (key,value)key act as a labels

#we can Also assign labels by passing 'index' argument for example

teachers=("rahul","shivani","pankaj","vishnio")
z=pd.Series(teachers,index=[1,2,3,4])
print(z)
i=pd.Series([v for v in range(0,11)])
print(i)
print(i.iloc[:])
print(i.iloc[-10:])
print(i.iloc[1:9])

print(i.iat[2])# same wroks as iloc

d=i.where(i%2==0)#it will return the values which satisfies this condition and for others NaN
print(d)

#there is an option where we can specify the value for false conditions 
e=i.where(i%2==0,'odd number')
print(e)
f=i.where(i%2==0,i**2)
print(f)