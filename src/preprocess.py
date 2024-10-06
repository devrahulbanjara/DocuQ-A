import pymupdf  

class PDFLoader: 
    def __init__(self, file): 
        self.pdf_document = pymupdf.open(file) 
    
    def pdf_text(self): 
        text = ""
        for page in self.pdf_document: 
            text += page.get_text() 
        return text 

if __name__ == "__main__": 
    pdf_path = "../../Downloads/CV.pdf"
    pdf_parser = PDFLoader(pdf_path)
    print(pdf_parser.pdf_text())