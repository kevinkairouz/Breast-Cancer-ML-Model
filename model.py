import matplotlib.pyplot as mpl
import pandas as pd  
import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier   
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler  

if __name__ == "__main__": 

    df = pd.read_csv("breast-cancer.csv") 
    df = df.replace("M", "1") 
    df = df.replace("B", "0") 
    df = df.astype({"diagnosis": int}) 

    #print(df.groupby("diagnosis")["diagnosis"].count()) #to see ratio of postiive & negative cases 

    Y = df["diagnosis"].to_numpy()
    X = df.drop("diagnosis", axis=1) 

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, stratify=Y, random_state=5)  


    

    model = KNeighborsClassifier()  

    model.fit(X_train, Y_train)

    Y_predicted = model.predict(X_test) 

    matrix = confusion_matrix(Y_test, Y_predicted)  
    
    truePos = matrix[0][0]
    falsePos = matrix[0][1] 

    falseNeg = matrix[1][0] 
    trueNeg = matrix[1][1]  

    trues = truePos + trueNeg 
    falses = falsePos + falseNeg 

    total = trues + falses 

    percent_correct = trues/total

    mpl.bar(["Got Correct", "Got Wrong"], [trues, falses]) 
    mpl.show() 

     

    
