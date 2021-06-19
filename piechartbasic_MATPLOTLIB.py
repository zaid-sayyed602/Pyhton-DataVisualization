import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df=pd.read_csv("Automobile_dataset.csv")
noc=df.groupby("num-of-cylinders").mean()
print(noc)
plt.pie(noc["index"])
plt.show()
