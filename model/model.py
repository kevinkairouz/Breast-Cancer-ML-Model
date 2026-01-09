#using the model that performed the best 
import pandas as pd   
import analysis 
from sklearn.model_selection import train_test_split  
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import recall_score 
from flask import Flask, jsonify, request, url_for, redirect, render_template  
import sqlite3 as sql 

#TODO: 
"""
1) create api and have it work with the prediction function 
2) make sure that at the end of the function in python we write to our sqlite3 database 
3) js/html/css to finish and deploy/test
"""

app_manager = Flask(__name__) 

@app_manager.route("/") 
def showMainPage(): 
    return render_template("index.html")

@app_manager.route("/predict")
def main(X_input):

    model = RandomForestClassifier(random_state=42, n_estimators= 100, max_depth=15) 
    
    df = pd.read_csv("breast-cancer.csv")  
    df = df.replace("M", "1") 
    df = df.replace("B", "0") 
    df = df.astype({"diagnosis": int}) 
    df = df.drop("id", axis = 1)

    Y = df["diagnosis"].to_numpy()
    X = df.drop("diagnosis", axis = 1).to_numpy()  

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, stratify=Y, random_state=42) 

    model.fit(X_train, Y_train)
    Y_pred = model.predict(X_test) 
    recall = recall_score(Y_test, Y_pred)
    print(f"Model Accuracy is {model.score(X_test, Y_test)} with a recall of {recall}")
    

    # Y_user_predicted = model.predict(X_input)
    # return Y_user_predicted

     
def run(): 
    app_manager.run() 

run()