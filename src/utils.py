import numpy as np
import pandas as pd
import os,sys

from src.exception import CustomException
from src.logger import logging

<<<<<<< HEAD
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error

=======
>>>>>>> 15cdd8f5b39d7203b742639ceab8128d70e41f2d
def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,"wb")as file_obj:
            pickle.dump(obj,file_obj)
        
    except Exception as e:
<<<<<<< HEAD
        raise CustomException(e,sys)
    
def evaluate_model(X_train,y_train,X_test,y_test,models):
    try:
        report={}
        for i in range(len(models)):
            model=list(models.values())[i]
            model.fit(X_train,y_train)

            y_test_pred=model.predict(X_test)

            test_model_score=r2_score(y_test,y_test_pred)

            report[list(models.keys())[i]]=test_model_score

        return report

    except Exception as e:
        return CustomException(e,sys)
=======
        raise CustomException(e,sys)
>>>>>>> 15cdd8f5b39d7203b742639ceab8128d70e41f2d
