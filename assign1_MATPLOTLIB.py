import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

d={"age":["13","12","11","22","17","19","22","25","20","32","30","28"],
   "size":["s","s","s","m","m","m","l","l","l","xl","xl","xl"]}
df=pd.DataFrame(d)
print("DATAFRAME\n",df)
df.to_csv("assign1.csv",index=False)
print("file created")
df1=pd.read_csv("assign1.csv")
choice=0
while(True):
    print("1.For BAR-CHART")
    print("2.For LINE-CHART")
    print("3.For HISTOGRAM")
    print("4.For PIE-CHART")
    print("5.Exit")
    choice=int(input("Enter your choice"))
    if(choice==1):
        plt.bar(df1["size"],df1["age"],color="y",width=0.8)
        plt.xlabel("sizes",fontsize=18)
        plt.ylabel("age",fontsize=18)
        plt.title("SIZE-CHART")
        plt.show()
    elif(choice==2):
        plt.plot(df1["size"],df1["age"],color="y",marker="o",ms=10,mec="w",mfc="g",linewidth=6)
        plt.xlabel("sizes",fontsize=18)
        plt.ylabel("age",fontsize=18)
        plt.title("SIZE-CHART")
        plt.show()
    elif(choice==3):
        plt.hist(df1["age"])
        plt.show()
    elif(choice==4):
        a=df1.groupby("size")
        b=a["age"].mean()
        label=("l","m","s","xl")
        plt.pie(b,labels=label,shadow=True)
        plt.legend()
        plt.show()
    elif(choice==5):
        print("Exited")
        break
        
