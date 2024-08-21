import pandas as pd
s=pd.Series(['a','c','v','v','b','m']) #reads as object,string or text,processing cannot be done in pandas
print(s)
#we have to declare the dtype="String"
#once it is declared as string type it can be processed as normal string
#funtions like str.upper(),str.lower() or str.len() can be processed

p=pd.Series(['ab','c','v','v','b','m'],dtype='string')
print(p)

#print(str.upper(s)) it will throw an error as dtype:object

print(p.str.upper())
print(p.str.len())