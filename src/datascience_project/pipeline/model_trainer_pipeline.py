from src.datascience_project.config.configuration import ConfigurationManager
from src.datascience_project.components.model_trainer import ModelTrainer
from src.datascience_project import logger

STAGE_NAME= "Model Trainer Stage"

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def initiate_model_training(self):
        try:
            config=ConfigurationManager()
            model_trainer_config=config.get_model_trainer_config()
            model_trainer=ModelTrainer(config=model_trainer_config)
            model_trainer.train()
        except Exception as e:
            raise e
        
if __name__=="__main__":
    try: 
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainerPipeline()
        obj.initiate_model_training()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\n X===============================X")
    except Exception as e:
        logger.exception(e)
        raise e        
