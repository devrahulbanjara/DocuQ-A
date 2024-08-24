from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline


class LLMInference: 
    def __init__(self, model_name = "deepset/roberta-base-squad2") -> None:
        self.model = AutoModelForQuestionAnswering.from_pretrained(model_name) 
        self.tokenizer = AutoTokenizer.from_pretrained(model_name) 
        self.pipeline = pipeline("question-answering", model = model_name, tokenizer = self.tokenizer)        


    def process_input(self,question, context): 
        QA_input = {"question":question, 
                    "context": context } 
        return QA_input
    

    def make_prediction(self, question, context): 
        res = self.pipeline(self.process_input(question, context))  
        return res 
