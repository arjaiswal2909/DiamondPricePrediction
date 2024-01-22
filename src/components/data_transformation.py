import sys,os

import numpy as np
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object


from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler,OrdinalEncoder

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

from dataclasses import dataclass
@dataclass 

class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()
    
    def get_data_transformation_object(self):
        try:
            logging.info('Data Transformation Initiated')

            categorical_columns=['cut','color','clarity']
            numerical_columns=['carat','depth','table','x','y','z']

            cut_categories=["Fair","Good","Very Good","Premium","Ideal"]
            clarity_categories=["I1","SI2","SI1","VS2","VS1","VVS2","VVS1","IF"]
            color_categories=["D","E","F","G","H","I","J"]

            logging.info('Data Transformation Pipeline intiated')

            num_pipeline=Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy="median")),
                    ('scaler',StandardScaler())
                ]
            )

            cat_pipeline=Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy="most_frequent")),
                    ('OrdinalEncoder',OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories])),
                    ('scaler',StandardScaler())
                ]
            )

            preprocessor=ColumnTransformer([
                ('num_pipeline',num_pipeline,numerical_columns),
                ('cat_pipeline',cat_pipeline,categorical_columns)
            ])
            logging.info('Data Transformation Completed')
            return preprocessor

        except Exception as e:
            logging.info('Exception occured in Data Transformation')
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_data_path,test_data_path):
        try:
            train_df=pd.read_csv(train_data_path)
            test_df=pd.read_csv(test_data_path)

            logging.info('Read train and test data completed')
<<<<<<< HEAD
            logging.info(f'Train Dataframe head : \n{train_df.head().to_string()}')
            logging.info(f'Test Dataframe head : \n{test_df.head().to_string()}')
=======
            logging.info('Train Dataframe head : \n{train_df.head().to_string()}')
            logging.info('Test Dataframe head : \n{test_df.head().to_string()}')
>>>>>>> 15cdd8f5b39d7203b742639ceab8128d70e41f2d

            preprocessor_obj=self.get_data_transformation_object()

            target_column='price'
            ## 
            drop_columns=[target_column]
            ## dividing into dependent and independent features

            input_feature_train_df=train_df.drop(columns=drop_columns,axis=1)
            target_feature_train_df=train_df[target_column]

            input_feature_test_df=test_df.drop(columns=drop_columns,axis=1)
            target_feature_test_df=test_df[target_column]

            ##Data Transoformation
            input_feature_train_arr=preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessor_obj.transform(input_feature_test_df)
            
            train_arr=np.c_[input_feature_train_arr,np.array(target_feature_train_df)]
            test_arr=np.c_[input_feature_test_arr,np.array(target_feature_test_df)]

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessor_obj
            )
            logging.info("Applying preprocessing object on training and testing datasets")

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )



        except Exception as e:
            raise CustomException(e,sys)

