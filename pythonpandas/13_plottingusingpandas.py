import pandas as pd
dataFrame=pd.read_csv("data.csv")
print(dataFrame.head())
print(dataFrame.plot())
print(dataFrame.plot(title="sample plot",figsize=(10,15)))
print(dataFrame.plot(x="Duration",y="Pulse",kind="scatter",legend=True))
print(dataFrame.plot(kind="hist",title="histogram"))