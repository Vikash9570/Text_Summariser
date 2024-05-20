import os
from src.logger import logging
from transformers import AutoTokenizer
# from datasets import load_dataset, load_from_disk
from textsummarizer.entity import DataTransformationConfig

class DataTransformation:
    def __init__(self,config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)

    def convert_examples_to_featues(self,example_batch):
        input_encoding = self.tokenizer(example_batch['article'],truncation=True)

        with self.tokenizer.as_target_tokenizer():
            target_encodings=self.tokenizer(example_batch["summary"],truncation=True)

        return {
            'input_ids': input_encoding['input_ids'],
            "attention_mask": input_encoding['attention_mask'],
            'labels': target_encodings['input_ids'] 

        }
    
    def convert(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()