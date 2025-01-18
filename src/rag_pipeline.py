from typing import List, Tuple
from .text_processor import TextProcessor
from .embeddings_manager import EmbeddingsManager
from .llm_client import LLMClientWrapper

class RAGPipeline:
    def __init__(self, 
                 pdf_path: str,
                 chunk_size: int = 2048,
                 chunk_overlap: int = 256
        ):
        self.pdf_path = pdf_path
        
        self.text_processor = TextProcessor(chunk_size, chunk_overlap)
        self.embeddings_manager = EmbeddingsManager()
        self.llm_client = LLMClientWrapper()
        
        self.chunks = self.text_processor.extract_text(pdf_path)
        self.embeddings_manager.create_embeddings(self.chunks, pdf_path)
        
    def query(self, question: str, top_k: int = 5) -> Tuple[str, List[Tuple[str, float]]]:
        chunks_with_scores = self.embeddings_manager.get_relevant_chunks(question, top_k)
        chunks = [chunk for chunk, _ in chunks_with_scores]
        
        response = self.llm_client.generate_response(question, chunks)
        return response, chunks_with_scores