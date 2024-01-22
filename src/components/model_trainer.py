import os,sys
import numpy as np
import pandas as pd

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object
from dataclasses import dataclass

from sklearn.linear_model import LinearRegression,Ridge,Lasso,ElasticNet
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from src.utils import evaluate_model

@dataclass
class ModelTrainerconfig:
    trained_model_file_path=os.path.join('artifacts','model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerconfig()

    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Splitting dependent and independent variable from train and test data")
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,:-1],
                test_array[:,:-1],
                test_array[:,:-1]
            )

            models={
                'Linear Regression':LinearRegression(),
                'Lasso':Lasso(),
                'Ridge':Ridge(),
                'ElasticNet':ElasticNet(),
                'Decision Tree':DecisionTreeClassifier(),
                'Random Forest':RandomForestClassifier()
            }
            model_report:dict=evaluate_model(X_train,y_train,X_test,y_test,models)
            print("\n------------")
            logging.info(f'Model Report:{model_report}')

            best_model_score=max(sorted(model_report.values()))

            best_model_name=list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model=models[best_model_name]

            print(f'Best model Score Name:{best_model_name},R2_score:{best_model_score}')
            print('\n--------------------')
            logging.info(f'Best model Name:{best_model_name}, R2_score:{best_model_score}')

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )


        except Exception as e:
            raise CustomException(e,sys)
        
