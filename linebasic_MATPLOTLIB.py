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
plt.plot(df["company"],df["price"],color="y",marker="o",ms=10,mec="w",mfc="g",linewidth=6)
plt.xlabel("company",fontsize=18)
plt.ylabel("prices",fontsize=18)
plt.title("Automobile")
plt.show()

#---MULTILE LINE DIAGRAM-----
'''x1=df["company"]
x2=df["price"]
x3=df["horsepower"]
plt.plot(x1,x2,color="y",marker="o",ms=10,mec="w",mfc="g",linewidth=6)
plt.plot(x1,x3,color="y",marker="o",ms=10,mec="w",mfc="g",linewidth=6)
plt.show()
'''
