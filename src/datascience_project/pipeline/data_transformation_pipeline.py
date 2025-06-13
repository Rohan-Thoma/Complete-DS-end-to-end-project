from src.datascience_project.config.configuration import ConfigurationManager
from src.datascience_project.components.data_transformation import DataTransformation # type: ignore
from src.datascience_project import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from src.datascience_project.entity.config_entity import DataTransformationConfig

STAGE_NAME = 'Data Transformation Stage'

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        config=ConfigurationManager()
        data_transformation_config=config.get_data_transformation_config()
        data_transformation=DataTransformation(config=data_transformation_config)
        data_transformation.train_test_splitting()

if __name__=="__main__":
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.initiate_data_transformation()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<< \n\n X==========================X")
    except Exception as e:
        logger.exception(e)
        raise e