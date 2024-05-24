from src.textsummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.logger import logging
from src.textsummarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from src.textsummarizer.pipeline.prediction import PredictionPipeline

STAGE_NAME="Data Ingestion Stage"
try:
    logging.info(f">> stage {STAGE_NAME} started")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logging.info(f'>> stage {STAGE_NAME} completed')
except Exception as e:
    logging.exception(e)
    raise e


STAGE_NAME="Data Transformation Stage"
try:
    logging.info(f">> stage {STAGE_NAME} started")
    data_transfromation = DataTransfromationTrainingPipeline()
    data_transfromation.main()
    logging.info(f'>> stage {STAGE_NAME} completed')
except Exception as e:
    logging.exception(e)
    raise e


STAGE_NAME="Model Trainer Stage"
try:
    logging.info(f">> stage {STAGE_NAME} started")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logging.info(f'>> stage {STAGE_NAME} completed')
except Exception as e:
    logging.exception(e)
    raise e



STAGE_NAME="prediction"
try:
    text="hi there this is an end to end project"
    logging.info(f">> stage {STAGE_NAME} started")
    model_trainer = PredictionPipeline()
    model_trainer.predict(text)
    logging.info(f'>> stage {STAGE_NAME} completed')
except Exception as e:
    logging.exception(e)
    raise e