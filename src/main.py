from model import LLMInference 
from preprocess import PDFLoader 

pdf_path = "../../Downloads/CV.pdf"

pdf_parser = PDFLoader(pdf_path)

context = pdf_parser.pdf_text() 
question = "Which school did he study in? "

llm = LLMInference()
res = llm.make_prediction(question, context )
print(f"Question: {question} \nAnswer: {res['answer']} \nConfidence: {res['score']}")