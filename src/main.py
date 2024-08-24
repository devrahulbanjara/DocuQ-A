from model import LLMInference 
from preprocess import PDFLoader 


pdf_path = "/mnt/c/Users/pawan/Documents/DocuQ-A/data/raw/cv-template.pdf"

pdf_parser = PDFLoader(pdf_path)

context = pdf_parser.pdf_text() 
question = "What is this Document about ? "

llm = LLMInference()
res = llm.make_prediction(question, context )
print(res)