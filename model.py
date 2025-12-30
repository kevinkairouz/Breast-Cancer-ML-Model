import matplotlib as mpl
import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier 

if __name__ == "__main__": 

    df = pd.read_csv("breast-cancer.csv") 
    df = df.replace("M", "1") 
    df = df.replace("B", "0") 
    df = df.astype({"diagnosis": int}) 

    #print(df.groupby("diagnosis")["diagnosis"].count()) #to see ratio of postiive & negative cases 

    Y = df["diagnosis"] 
    X = df.drop("diagnosis", axis=1) 

     

    
