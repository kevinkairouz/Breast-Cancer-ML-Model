#used for algorithm analysis measuring effectiveness of each algorithm that was used 
#and algorithm that i used   
import pandas as pd
import matplotlib.pyplot as mpl  
from sklearn.linear_model import LogisticRegression 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.tree import DecisionTreeClassifier 
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.metrics import classification_report 
from sklearn.model_selection import GridSearchCV 

if __name__ == "__main__": 

    RF = RandomForestClassifier() 
    DT = DecisionTreeClassifier() 
    KN = KNeighborsClassifier() 

    RF_params = {"n_estimators": [1,10,100,500,700,1000], "max_depth": [1,5,10,15,20,30]}  

    RF_grid = GridSearchCV(RF)
 





