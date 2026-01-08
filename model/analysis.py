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
from sklearn.model_selection import RandomizedSearchCV 
from sklearn.model_selection import train_test_split





#TODO  
""" 
EDITS: give each ML algorithm a random state = 42 to ensure consistency
 
1) compare the precision and recall among the models and plot it on bar chart 
2) compare the score/accraucy and plot it on the bar chart -- Completed X 
3) if possible compare each model variation using subplots of the precision, recall, score/accuracy
"""

if __name__ == "__main__":  

    modelNames = ["Random Forest", "Decision Tree", "K-Neighbors", "Logistic-Regression"]

    bestModel = None

  

    df = pd.read_csv("breast-cancer.csv")  
    df = df.replace("M", "1") 
    df = df.replace("B", "0") 
    df = df.astype({"diagnosis": int}) 
    df = df.drop("id", axis = 1)

    Y = df["diagnosis"].to_numpy()
    X = df.drop("diagnosis", axis = 1).to_numpy()  

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, stratify=Y, random_state=42) 

    RF = RandomForestClassifier(random_state=42)
    DT = DecisionTreeClassifier(random_state=42)
    KN = KNeighborsClassifier()
    LR = LogisticRegression(random_state=42) 

    RF_params = {"n_estimators": [1,10,100,500,700,1000], "max_depth": [1,5,10,15,20,30]} 
    DT_params = {"max_depth": [1,5,10,15,20,30]} 
    KN_params = {"n_neighbors": [5,10,15,20,25]}  
    LR_params = {"C": [1,5,15,50,100]} 


    RF_model = RandomizedSearchCV(RF, RF_params) 
    DT_model = GridSearchCV(DT, DT_params) 
    KN_model = GridSearchCV(KN, KN_params) 
    LR_model = RandomizedSearchCV(LR, LR_params) 

    RF_model.fit(X_train, Y_train) 
    DT_model.fit(X_train, Y_train) 
    KN_model.fit(X_train, Y_train) 
    LR_model.fit(X_train, Y_train)  

    print(f"Decision Tree Score: {DT_model.best_score_} with {DT_model.best_params_}")  
    print(f"Random Forest Score: {RF_model.best_score_} with {RF_model.best_params_}")
    print(f"K Neighbors Score is {KN_model.best_score_} with {KN_model.best_params_}") 
    print(f"Logsitic Regression score {LR_model.best_score_} with {LR_model.best_params_ }")

    bar_colors = ['tab:red', 'tab:blue', 'tab:black', 'tab:pink']
    mpl.bar(["Random Forest", "Decision Tree", "K Neighbors", "Logistic Regression"], [DT_model.best_score_,RF_model.best_score_,KN_model.best_score_,LR_model.best_score_], colors = bar_colors )

    mpl.show()  

    bestModel = max(DT_model.best_score_,RF_model.best_score_,KN_model.best_score_,LR_model.best_score_)

    






    



 





