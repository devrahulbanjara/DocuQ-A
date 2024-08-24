import pymupdf  



class PDFLoader: 
    def __init__(self, file): 
        self.pdf_document = pymupdf.open(file) 
    

    def pdf_text(self): 
        text = ""
        for page in self.pdf_document: 
            text += page.get_text() 
        return text 
