import pandas as pd
dataFrame=pd.DataFrame({"problem":["headche","fever",'cough','sore throat','allergies','indigestion'],
    "medicine":["anacin",'dolo 650','strepsils','tylenol','benadryl','lopermide'],
    "dosage":["one time","3times a day,for 3 days","3times a day,for 2 days","3times a day","1 time in night","2times a day"]},index=[1,2,3,4,5,6]
)
#print(dataFrame)
for i in dataFrame.index:    #iteration using for loop
    print(dataFrame["problem"][i],dataFrame["medicine"][i],dataFrame["dosage"][i])
#iteration using iloc method
for i in range(len(dataFrame)):
    print(dataFrame.iloc[i,0],dataFrame.iloc[i,1],dataFrame.iloc[i,2])
#iteration using iterrows()
for index,row in dataFrame.iterrows():  
    print(row["medicine"],row["dosage"])  
    