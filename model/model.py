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
1) finish api creation/flask functionality 
2) include in the main function for prediction to write each prediction to our sqlite3 database 
ps. make the sqlite db global scope so function has access to it 
"""

app_manager = Flask(__name__) 

feature_names = [
    'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean',
    'compactness_mean', 'concavity_mean', 'concave_points_mean', 'symmetry_mean',
    'fractal_dimension_mean', 'radius_se', 'texture_se', 'perimeter_se', 'area_se',
    'smoothness_se', 'compactness_se', 'concavity_se', 'concave_points_se',
    'symmetry_se', 'fractal_dimension_se', 'radius_worst', 'texture_worst',
    'perimeter_worst', 'area_worst', 'smoothness_worst', 'compactness_worst',
    'concavity_worst', 'concave_points_worst', 'symmetry_worst', 'fractal_dimension_worst'
]


@app_manager.route("/") 
def showMainPage(): 
    return render_template("index.html")

@app_manager.route("/predict", methods = ["POST"])
def main():

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