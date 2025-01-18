import os
import dotenv
import time
from src.rag_pipeline import RAGPipeline

def handle_query(rag: RAGPipeline, user_input: bool = False, question: str = None):
    if not user_input and not question:
        raise ValueError("Example question is required")
    
    if user_input:
        question = input("Question: ")
    else:
        print("Question: ", question)
    
    response, _ = rag.query(question)
    print("\nResponse:")
    print(response)
    print("-" * 80)

def main():
    dotenv.load_dotenv()
    
    pdf_path = os.path.join("documents", "The Ultimate Guide to Tarot - A Beginner.txt")
    rag = RAGPipeline(pdf_path=pdf_path)
    
    questions = [
        "Как связаны Арканы Солнца и Луны?",
        "Какой смысл у Аркана Королевы?",
        "Какой аркан отвечает за неожиданные перемены и почему?"
    ]
    
    for question in questions:
        handle_query(rag, question=question)
        time.sleep(3)
        
    print("Now you can start asking your own questions!")
    
    while True:
        handle_query(rag, user_input=True)

if __name__ == "__main__":
    main() 