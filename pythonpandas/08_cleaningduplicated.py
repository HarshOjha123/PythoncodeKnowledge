'''To discover duplicates, we can use the duplicated() method.
The duplicated() method returns a Boolean values for each row:'''
import pandas as pd
df=pd.read_csv("filename")
print(df.duplicated())

# To remove duplicates, use the drop_duplicates() method.
df.drop_duplicates(inplace = True)

# Remember: The (inplace = True) will make sure that the method does NOT return a new DataFrame, but it will remove all duplicates from the original DataFrame.

