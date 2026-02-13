import numpy as np
import pandas as pd

arr = np.array([10,30,20,5,6,200])

print("array:",arr)
print("sum :",np.sum(arr))
print("mean:",np.mean(arr))
print("median:",np.median(arr))
print("max:",np.max(arr))
print("multiply:",arr*2)

data={
    "Name": ["Kiran","Anitha","Ravi"],
    "Age" : [24,25,26],
    "City" : ["Banglore","Chennai","Hyderbad"]


}

df=pd.DataFrame(data)
print(df)

print(type(df))
print(df["Name"])
print(df["Age"]>25)
print(df["City"]=="Banglore")
df['salary']=[50000,20000,60000
              ]