from src.datascience_project import logger
from src.datascience_project.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline

STAGE_NAME = 'Data Ingestion Stage'

try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<< \n\n X==========================X")
except Exception as e:
    logger.exception(e)
    raise e


