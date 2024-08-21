import pandas as pd
# One way to fix wrong values is to replace them with something else.
df=pd.read_csv("filename")
df.loc[3,'columnname']=45

# To replace wrong data for larger data sets you can create some rules, e.g. set some boundaries for legal values, and replace any values that are outside of the boundaries.

for x in df.index:
  if df.loc[x, "columnname"] > 120:
    df.loc[x, "columnname"] = 120
    
# Another way of handling wrong data is to remove the rows that contains wrong data.
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True) 
