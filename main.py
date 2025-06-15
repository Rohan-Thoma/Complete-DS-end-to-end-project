from src.datascience_project import logger
from src.datascience_project.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience_project.pipeline.data_validation_pipeline import DataValidationTrainingPipeline 
from src.datascience_project.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline 
from src.datascience_project.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.datascience_project.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline
import os

STAGE_NAME = 'Data Ingestion Stage'

try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<< \n\n X==========================X")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Data Validation Stage'

try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.initiate_data_validation()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<< \n\n X==========================X")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = 'Data Transformation Stage'

try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.initiate_data_transformation()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<< \n\n X==========================X")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME= "Model Trainer Stage"

try: 
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainerPipeline()
        obj.initiate_model_training()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\n X===============================X")
except Exception as e:
        logger.exception(e)
        raise e   

# MLFLOW_TRACKING_URI=os.getenv("MLFLOW_TRACKING_URI")
# MLFLOW_TRACKING_USERNAME=os.getenv("MLFLOW_TRACKING_USERNAME")
# MLFLOW_TRACKING_PASSWORD=os.getenv("MLFLOW_TRACKING_PASSWORD")

STAGE_NAME = 'Model Evaluation Stage'

try:
        logger.info(f">>>>>>stage {STAGE_NAME} started <<<<<<<")
        obj = ModelEvaluationPipeline()
        obj.initiate_model_evaluation()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\n X===============================X")
except Exception as e:
        logger.exception(e)
        raise e  