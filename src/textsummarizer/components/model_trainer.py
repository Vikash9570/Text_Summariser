# from transformers import TraningArguments, Trainer
# from datasets import load_dataset, load_from_disk
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
# from transformers import DataCollectionForSeq2Seq
import torch
from src.textsummarizer.entity import ModelTrainerConfig
import os

class ModelTrainer:
    def __init__(self,config: ModelTrainerConfig):
        self.config = config

    def train(self):
        device ="cuda" if torch.cuda.is_available() else 'cpu'
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        # seq2seq_data_collector = DataCollectionForSeq2Seq(tokenizer,model=model_pegasus)

        # dataset_data_csv=load_from_disk(self.config.data_path)
        
        # training_arg=TraningArguments(
        #     output_dir=self.config.root_dir, num_train_epochs=1, wrap_steps=500,
        #     per_device_train_batch_size=1, per_device_eval_batch_size=1,
        #     weight_decay=0.01, logging_steps=10,
        #     evaluation_strategy='steps', eval_steps=500,save_steps =1e6,
        #     gradient_accumulation_steps =16
        # )
        # trainer =Trainer(model = model_pegasus, args=training_arg,
        #             tokenizer=tokenizer,data_collector=seq2seq_data_collector,
        #             train_dataset=dataset_data_csv,
        #             eval_dataset=dataset_data_csv)
        
        # trainer.train()

        # saving model
        model_pegasus.save_pretrained(os.path.join(self.config.root_dir,'pegasus-large-model'))
        
        # save tokenizer
        tokenizer.save_pretrained(os.path.join(self.config.root_dir,'tokenizer'))
         
