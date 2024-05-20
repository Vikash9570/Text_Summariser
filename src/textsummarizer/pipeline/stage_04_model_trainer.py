from src.textsummarizer.config.configuration import ConfigurationManager
from src.textsummarizer.components.model_trainer import ModelTrainer

from src.logger import logging
from src.textsummarizer.constants import CONFIG_FILE_PATH






class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config_obj = ConfigurationManager(CONFIG_FILE_PATH)
        model_trainer_config = config_obj.get_model_trainer_config()
        model_trainer_obj = ModelTrainer(config=model_trainer_config)
        model_trainer_obj.train()