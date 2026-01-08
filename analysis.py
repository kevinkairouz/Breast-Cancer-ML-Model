#used for algorithm analysis measuring effectiveness of each algorithm that was used 
#and algorithm that i used in order to determine most effective algorithm to use to catch M and B cases  
import pandas as pd
import matplotlib.pyplot as mpl  
from sklearn.linear_model import LogisticRegression 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.tree import DecisionTreeClassifier 
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.metrics import classification_report 
from sklearn.model_selection import GridSearchCV  
from sklearn.model_selection import train_test_split
import numpy as np 


#TODO  
"""
1) compare the precision and recall among the models and plot it on bar chart 
2) compare the score/accraucy and plot it on the bar chart  
3) if possible compare each model variation using subplots of the precision, recall, score/accuracy
"""

if __name__ == "__main__": 

    scores = np.array([])  

    df = pd.read_csv("breast-cancer.csv")  
    df = df.replace("M", "1") 
    df = df.replace("B", "0") 
    df = df.astype({"diagnosis": int}) 
    df = df.drop("id", axis = 1)

    Y = df[["diagnosis"]] 
    X = df.drop("diagnosis", axis = 1) 

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, stratify=Y, random_state=42) 

    RF = RandomForestClassifier()
    DT = DecisionTreeClassifier()
    KN = KNeighborsClassifier()
    LR = LogisticRegression() 

    RF_params = {"n_estimators": [1,10,100,500,700,1000], "max_depth": [1,5,10,15,20,30]} 
    DT_params = {"max_depth": [1,5,10,15,20,30]} 
    KN_params = {"n_neighbors": [5,10,15,20,25]}  
    LR_params = {"C": [1,5,15,50,100]} 


    RF_model = GridSearchCV(RF, RF_params) 
    





    



 





