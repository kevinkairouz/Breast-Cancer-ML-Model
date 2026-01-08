#using the model that performed the best 
#printing out its score to the console 

import pandas as pd  
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler 
from sklearn.model_selection import GridSearchCV 
from flask import Flask 


if __name__ == "__main__": 

    df = pd.read_csv("breast-cancer.csv") 
    df = df.replace("M", "1") 
    df = df.replace("B", "0") 
    df = df.astype({"diagnosis": int}) 
    df = df.drop("id", axis = 1)  

    # print(df.groupby("diagnosis")["diagnosis"].count()) done to see amount of M & B 



    # print(df.info()) done for testing purpose




    

     

    
