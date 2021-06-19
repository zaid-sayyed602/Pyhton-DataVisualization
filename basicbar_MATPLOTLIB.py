import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df=pd.read_csv("Automobile_dataset.csv")
print(df.isna().sum())
avg=df["price"].agg(np.max)
print("THE AVG VALUE OF PRICES IN THE COLUMN IS",avg)
df["price"]=df["price"].fillna(avg)
print("MISSING VALUES HAS BEEN SUCCESSFULLY FILLED WITH AVERAGE")
print("UPDATED\n",df.isna().sum())
plt.bar(df["company"],df["price"],color="y",width=0.8)
plt.xlabel("company",fontsize=18)
plt.ylabel("prices",fontsize=18)
plt.title("Automobile")
plt.show()
