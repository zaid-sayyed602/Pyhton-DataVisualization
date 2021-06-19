import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
titanic=sb.load_dataset("titanic")
print(titanic)
titanic.to_csv("titanicseaborn.csv",index=False)
choice=0
while(True):
    print("1.BAR")
    print("2.scatter")
    print("3.relplot")
    print("4.histogram")
    print("5.countplot")
    print("6.pointplot")
    print("7.joint plot")
    print("8.Pairplot")
    choice=int(input("Enter your choice here\n"))
    if(choice==1):
        sb.set_style("darkgrid")
        sb.set_context("poster")
        sb.despine()##used to remove the top and the right lines of the plot
        sb.barplot(x="sex",y="age",hue="pclass",data=titanic)
        plt.show()
#---for horizontal---
##sb.barplot(y="embark_town",x="age",data=titanic,orient="h")
    elif(choice==2):
        ##plotting used by matplotlib
        sb.set_style("dark")
        sb.despine()##used to remove the top and the right lines of the plot
        sb.set_context("poster")
        plt.scatter("sex","fare",data=titanic)
        plt.show()
    elif(choice==3):
        #---plottind used by seaborn
        sb.relplot(x="sex",y="fare",hue="who",col="embark_town",col_wrap=3,data=titanic)
        ##kind="line"
        plt.show()
    elif(choice==4):
        sb.distplot(titanic["pclass"])  
        plt.show()
    elif(choice==5):
        sb.countplot(x="pclass",hue="who",data=titanic,palette="magma")
        plt.show()
    elif(choice==6):
        sb.pointplot(x="who",y="survived",data=titanic)
        plt.show()
    elif(choice==7):
        ##sb.jointplot(x="sex",y="age",data=titanic)
        sb.jointplot(kind="hex",x="pclass",y="age",data=titanic)
        plt.show()
    elif(choice==8):
        sb.pairplot(titanic,hue="who",diag_kind="kde",kind="scatter")
        plt.show()
