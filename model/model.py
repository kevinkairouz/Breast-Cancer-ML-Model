#using the model that performed the best 


import pandas as pd   
import analysis 
from sklearn.model_selection import train_test_split  
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler 
from sklearn.model_selection import GridSearchCV 
from flask import Flask, jsonify, request   
import sqlite3 as sql 

if __name__ == "__main__": 

    model = RandomForestClassifier(random_state=42, n_estimators= 100, max_depth=15)

# Random Forest Score: 0.9647606019151848 with {'n_estimators': 100, 'max_depth': 15}


    

     

    
