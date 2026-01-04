import matplotlib.pyplot as mpl
import pandas as pd  
import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier   
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler  

from sklearn.metrics import classification_report

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

    # print(recall_score(Y_test, Y_predicted)) 
    # print(precision_score(Y_test, Y_predicted)) 
    # print()    
   
    # print(recall_score(Y_test, Y_predicted))

    print(classification_report(Y_test, Y_predicted))

    

     

    
