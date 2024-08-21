'''A great aspect of the Pandas module is the corr() method.
The corr() method calculates the relationship between each column in your data set.
The examples in this page uses a CSV file called: 'data.csv'.'''

#corr() metod

import pandas as pd
df=pd.read_csv("data.csv")
print(df.corr().to_string())

# Note: The corr() method ignores "not numeric" columns.
# The Result of the corr() method is a table with a lot of numbers that represents how well the relationship is between two columns.
# The number varies from -1 to 1.
#  It depends on the use, but I think it is safe to say you have to have at least 0.6 (or -0.6) to call it a good correlation.

