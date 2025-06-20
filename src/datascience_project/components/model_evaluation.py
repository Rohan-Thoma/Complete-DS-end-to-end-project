import pandas as pd 
import os 
from sklearn.metrics import mean_squared_error, mean_absolute_error,r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np 
import joblib 
from pathlib import Path 
from src.datascience_project.utils.common import save_json

from src.datascience_project.constants import *
from src.datascience_project.entity.config_entity import ModelEvaluationConfig
from dotenv import load_dotenv

load_dotenv() # This is to load all the env variables which are the dagshub credentials and stuff etc.

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config 

    def eval_metrics(self, actual, pred):
        rmse= np.sqrt(mean_absolute_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2 
    
    def log_into_mlflow(self):

        test_data = pd.read_csv(self.config.test_data_dir)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme  


        with mlflow.start_run():

            predicted_qualities = model.predict(test_x)

            (rmse,mae,r2)= self.eval_metrics(test_y, predicted_qualities)

            #saving the metrics as local
            scores = {'rmse':rmse,'mae':mae,'r2':r2}
            save_json(path=Path(self.config.metric_file_name), data= scores)

            mlflow.log_params(self.config.all_params)
            mlflow.log_metric("rmse",rmse)
            mlflow.log_metric("mae",mae)
            mlflow.log_metric("r2",r2)

            #Model registry does not work with file store
            if tracking_url_type_store != 'file':

                #register the model
                # There are other ways to use the model registry , which depends on the use caes
                # pLease refer to the doc for more information
                # https://mlflow.org/docs/latest/model-registry.html#api-workflow

                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticNetModel")
            else:
                mlflow.sklearn.log_model(model, "model")     
