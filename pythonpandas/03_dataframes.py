#Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
#Series is like a column, a DataFrame is the whole table.
import pandas as pd
x={'mustang':["india","america","china","japan"],
   'rollsroyce':["america","uk","india","japan"],
   'supra':["america","uk","australia","china"]}
y=pd.DataFrame(x,index=[1,2,3,4])
print(y)

#Pandas use the 'loc' attribute to return one or more specified row(s)
print(y.loc[2])#o/p will be series
print(y.loc[[1,3]])#using [] then o/p will be dataframe

z=pd.DataFrame()
z=pd.read_csv("data.csv")
print(z)

print(z.head())  # top 5 we can specify the no. in head function upto which we want to see from top

print(z.tail(10))  # last 5  we can specify the no. in tail function upto which we want to see from below

print(y.values)# return data in the form of lists

#if data set is too big we can divide data in the no of chunks of same size
l=pd.read_csv('data.csv',chunksize=2)
for chunk in l:
   print(chunk, "\n")
print("\n") 

# I M P O R T A N T  

#we can specify conditions and get the required data sets too for example
k=pd.read_csv('data.csv')
k=k[k['Pulse']==100]
print(k)