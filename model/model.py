#using the model that performed the best 
#printing out its score to the console  

#importing analysis will allow me to use the most_accurate model and then print out its score 
#and then allow for me to host it on api  

#then can use html and css and js to give interactiveness and or console interactiveness 


import pandas as pd   
import analysis 
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler 
from sklearn.model_selection import GridSearchCV 
from flask import Flask, jsonify, request   
import sqlite3 as sql 










if __name__ == "__main__": 

    modelManager = analysis  

    print(modelManager.bestModel)

    # df = pd.read_csv("model/breast-cancer.csv") 
    # df = df.replace("M", "1") 
    # df = df.replace("B", "0") 
    # df = df.astype({"diagnosis": int}) 
    # df = df.drop("id", axis = 1)  

    # print(df.groupby("diagnosis")["diagnosis"].count()) done to see amount of M & B 



    # print(df.info()) done for testing purpose




    

     

    
