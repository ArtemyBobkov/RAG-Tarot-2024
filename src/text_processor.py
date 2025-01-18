import pymupdf
from typing import List
from langchain.text_splitter import RecursiveCharacterTextSplitter

class TextProcessor:
    def __init__(
        self, 
        chunk_size: int = 2048, 
        chunk_overlap: int = 256,
        minimum_line_length: int = 10,
    ):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size, 
            chunk_overlap=chunk_overlap
        )
        self.minimum_line_length = minimum_line_length
        
    def extract_text(self, pdf_path: str) -> List[str]:
        text = ""
        if pdf_path.endswith(".pdf"):
            doc = pymupdf.open(pdf_path)
            for page in doc:
                text += page.get_text()
        else:
            with open(pdf_path, "r") as file:
                text = file.read()
        
        text = "\n".join([
            line for line in text.splitlines() 
            if len(line.split()) > self.minimum_line_length
        ])
        
        chunks = self.text_splitter.split_text(text)
        return chunks 