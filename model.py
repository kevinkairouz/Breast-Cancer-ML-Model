import matplotlib as mpl
import pandas as pd  
import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier  
from sklearn.preprocessing import StandardScaler

if __name__ == "__main__": 

    df = pd.read_csv("breast-cancer.csv") 
    df = df.replace("M", "1") 
    df = df.replace("B", "0") 
    df = df.astype({"diagnosis": int}) 

    #print(df.groupby("diagnosis")["diagnosis"].count()) #to see ratio of postiive & negative cases 

    Y = df["diagnosis"].to_numpy()
    X = df.drop("diagnosis", axis=1) 

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, stratify=Y)  


    

    model = KNeighborsClassifier() 

    model.fit(X_train, Y_train) 

    acc_score = model.score(X_test, Y_test) 
    print(acc_score) 




     

    
