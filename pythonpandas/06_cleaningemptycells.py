'''Data cleaning means fixing bad data in your data set.

Bad data could be:

1)Empty cells
2)Data in wrong format
3)Wrong data
4)Duplicates'''
import pandas as pd
# Note: By default, the dropna() method returns a new DataFrame, and will not change the original.

df=pd.read_csv("data.csv")
newdf=df.dropna()
print(newdf.to_string())

#  Now, the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containing NULL values from the original DataFrame.

'''Another way of dealing with empty cells is to insert a new value instead.
This way you do not have to delete entire rows just because of some empty cells.
The fillna() method allows us to replace empty cells with a value:'''

import pandas as pd
df = pd.read_csv('data.csv')
df.fillna(130, inplace = True)

# Replace Only For Specified Columns
df["Calories"].fillna(130, inplace = True)


# Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column:
# the empty values are replaced with one of them 

