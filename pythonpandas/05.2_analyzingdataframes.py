# The head() method returns the headers and a specified number of rows, starting from the top.
import pandas as pd
read=pd.read_csv("data.csv")
print(read.head(10))#print from top i.e 0 to 9
# Note: if the number of rows is not specified, the head() method will return the top 5 rows.


#The tail() method returns the headers and a specified number of rows, starting from the bottom.
print(read.tail(10))

# The DataFrames object has a method called info(), that gives you more information about the data set.

print(read.info())

''' The info() method also tells us how many Non-Null values there are present in each column, and in our data set it seems like there are 164 of 169 Non-Null values in the "Calories" column.
Which means that there are 5 rows with no value at all, in the "Calories" column, for whatever reason.'''

