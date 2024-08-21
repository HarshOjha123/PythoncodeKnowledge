import pandas as pd
r=pd.Series(['AB+','AB-','A+','A-','B+','B-','O+','O-','A-','AB+','A+','B+','O+','O-','AB-','B-'], dtype="category" )
print(r)

#categorical data can be created using categorical class
c=pd.Categorical(['A+','A-','B+','B-','C+','C-','F'])
print(c)