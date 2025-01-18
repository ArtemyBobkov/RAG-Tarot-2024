import os
from typing import List
from yandex_chain import YandexLLM, YandexGPTModel

class LLMClientWrapper:
    
    system_prompt = """
        You are a helpful AI assistant. Use the provided context to answer the question. 
        If you cannot find the answer in the context, say so. Base your answer only on the provided context. 
        Do not use your own knowledge even if context does not contain the answer. 
        Use as much useful information from context as possible.
        Your answer should be in the language of the original question.
    """
    
    def __init__(self):
        if not os.environ['YANDEX_API_KEY']:
            raise ValueError("API key not found")
        if not os.environ['YANDEX_FOLDER_ID']:
            raise ValueError("Folder ID not found")
        
        self.client= YandexLLM(
            folder_id=os.environ['YANDEX_FOLDER_ID'],
            api_key=os.environ['YANDEX_API_KEY'],
            model=YandexGPTModel.Pro,
            instruction_text=self.system_prompt,
        )
        
    def generate_response(self, question: str, context_chunks: List[str]) -> str:
        context = "\n\n".join(context_chunks)
        
        messages = [
            {
                "role": "user",
                "text": f"<context>\n{context}\n</context>\n<question>\n{question}\n</question>"
            }
        ]
        response = self.client._generate_messages(messages)
        return response 