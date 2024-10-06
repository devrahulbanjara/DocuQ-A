from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
import torch

class LLMInference: 
    def __init__(self, model_name = "deepset/roberta-base-squad2") -> None:
        self.model = AutoModelForQuestionAnswering.from_pretrained(model_name) 
        self.tokenizer = AutoTokenizer.from_pretrained(model_name) 
        self.device = 0 if torch.cuda.is_available() else -1
        self.nlp = pipeline('question-answering', model=model_name, tokenizer=model_name, device=self.device)
    
    def process_input(self,question, context): 
        QA_input = {"question":question, 
                    "context": context } 
        return QA_input

    def make_prediction(self, question, context): 
        res = self.nlp(self.process_input(question, context))  
        return res 
