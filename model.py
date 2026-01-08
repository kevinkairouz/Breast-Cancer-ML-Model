import pandas as pd  
from sklearn.model_selection import train_test_split 
from sklearn.metrics import classification_report 

from sklearn.preprocessing import StandardScaler 
from sklearn.model_selection import GridSearchCV


if __name__ == "__main__": 

    df = pd.read_csv("breast-cancer.csv") 
    df = df.replace("M", "1") 
    df = df.replace("B", "0") 
    df = df.astype({"diagnosis": int}) 
    df = df.drop("id", axis = 1)  


    # print(df.info()) done for testing purpose




    

     

    
