from typing import List, Tuple
from langchain_community.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore
from yandex_chain import YandexEmbeddings
import os
from tqdm import tqdm
import faiss
import time

class EmbeddingsManager:
    def __init__(self, save_dir: str = "embeddings_cache"):
        if not os.environ['YANDEX_API_KEY']:
            raise ValueError("API key not found")
        if not os.environ['YANDEX_FOLDER_ID']:
            raise ValueError("Folder ID not found")
        
        self.embeddings = YandexEmbeddings(
            folder_id=os.environ['YANDEX_FOLDER_ID'], 
            api_key=os.environ['YANDEX_API_KEY']
        )
        self.save_dir = save_dir
        self.vector_store = None
        
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
    
    def _get_cache_path(self, pdf_path: str) -> str:
        pdf_name = os.path.basename(pdf_path)
        return os.path.join(self.save_dir, f"{pdf_name}.faiss")
    
    def _initialize_vector_store(self):
        embedding_size = len(self.embeddings.embed_query("test"))
        index = faiss.IndexFlatL2(embedding_size)
        self.vector_store = FAISS(
            embedding_function=self.embeddings,
            index=index,
            docstore=InMemoryDocstore(),
            index_to_docstore_id={}
        )
    
    def create_embeddings(self, texts: List[str], pdf_path: str) -> None:
        cache_path = self._get_cache_path(pdf_path)
        
        if os.path.exists(cache_path) and os.path.getsize(cache_path) > 0:
            print(f"Loading embeddings from cache {cache_path}")
            self._initialize_vector_store()
            self.vector_store = FAISS.load_local(
                cache_path, 
                self.embeddings,
                allow_dangerous_deserialization=True
            )
            print("Embeddings loaded!")
        else:
            print("Creating embeddings...")
            self._initialize_vector_store()
            
            for text in tqdm(texts):
                time.sleep(3)
                self.vector_store.add_texts([text])
            
            self.vector_store.save_local(cache_path)
            print(f"Embeddings saved to {cache_path}")
    
    def get_relevant_chunks(self, query: str, top_k: int = 5) -> List[Tuple[str, float]]:
        results = self.vector_store.similarity_search_with_score(query, k=top_k)
    
        return [(doc.page_content, score) for doc, score in results] 