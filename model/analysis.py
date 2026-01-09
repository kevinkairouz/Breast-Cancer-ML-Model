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
from sklearn.metrics import recall_score 
from sklearn.metrics import precision_score



if __name__ == "__main__":  
    
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

    Y_pred_RF = RF_model.predict(X_test)
    Y_pred_DT = DT_model.predict(X_test) 
    Y_pred_KN = KN_model.predict(X_test)
    Y_pred_LR = LR_model.predict(X_test)

    print(f"Decision Tree Score: {DT_model.best_score_} with {DT_model.best_params_}")  
    print(f"Random Forest Score: {RF_model.best_score_} with {RF_model.best_params_}")
    print(f"K Neighbors Score is {KN_model.best_score_} with {KN_model.best_params_}") 
    print(f"Logsitic Regression score {LR_model.best_score_} with {LR_model.best_params_ }")

    bar_colors = ["red","black","green","orange"]
    
    
    bestModel = max(DT_model.best_score_,RF_model.best_score_,KN_model.best_score_,LR_model.best_score_)

    
    rf_recall = recall_score(Y_test, Y_pred_RF)
    dt_recall = recall_score(Y_test, Y_pred_DT) 
    kn_recall = recall_score(Y_test, Y_pred_KN)
    lr_recall = recall_score(Y_test, Y_pred_LR)


    rf_prec = precision_score(Y_test, Y_pred_RF)
    dt_prec = precision_score(Y_test, Y_pred_DT) 
    kn_prec = precision_score(Y_test, Y_pred_KN)
    lr_prec = precision_score(Y_test, Y_pred_LR)



    fig, axis = mpl.subplots(1,3) 
    axis[0].bar(["RForest", "DTree", "KNN", "LogReg"], [RF_model.best_score_, DT_model.best_score_, KN_model.best_score_,LR_model.best_score_], color = bar_colors )  
    axis[0].set_title("Acc Score")
    axis[1].bar(["RForest", "DTree", "KNN", "LogReg"], [rf_recall,dt_recall,kn_recall,lr_recall], color = bar_colors)
    axis[1].set_title("Recall Score")
    axis[2].bar(["RForest", "DTree", "KNN", "LogReg"], [rf_prec,dt_prec,kn_prec,lr_prec], color = bar_colors) 
    axis[2].set_title("Precision Score") 
    mpl.show()  
    

    # sample_indices = range(len(Y_test))
    # axis[1,1].scatter(sample_indices, Y_pred_RF, label="RForest", alpha=0.6)
    # axis[1,1].scatter(sample_indices, Y_pred_DT, label="DTree", alpha=0.6)
    # axis[1,1].scatter(sample_indices, Y_pred_KN, label="KNN", alpha=0.6)
    # axis[1,1].scatter(sample_indices, Y_pred_LR, label="LogReg", alpha=0.6)
    # axis[1,1].legend()
    # axis[1,1].set_title("Predictions") 
   






    



    



 





