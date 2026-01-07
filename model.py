import matplotlib.pyplot as mpl
import pandas as pd  
import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn.metrics import classification_report 
from sklearn.linear_model import LinearRegression 
from sklearn.preprocessing import StandardScaler 
from sklearn.model_selection import GridSearchCV


if __name__ == "__main__": 

    df = pd.read_csv("breast-cancer.csv") 
    df = df.replace("M", "1") 
    df = df.replace("B", "0") 
    df = df.astype({"diagnosis": int}) 


    Y = df["diagnosis"].to_numpy()
    X = df.drop("diagnosis", axis=1)   

    

  
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, stratify=Y, random_state=42)  

    scaler = StandardScaler() 
    model = LinearRegression()  



    

     

    
