from src.textsummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline


class PredictionPipeline:
    def __init__(self) :
        self.config = ConfigurationManager().get_model_evaluation_config()

        

    def predict(self,text):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        gen_kwargs = {'length_penalty': 2.0, "num_beams": 5, "max_length": 100}

        pipe = pipeline("summarization", model= self.config.model_path, tokenizer=tokenizer)

        print('Article:')
        print(text)

        output=pipe(text, **gen_kwargs)[0]["summary_text"]
        print("\nModel Summary:")
        # print(output)
        return output