# src/main.py

from .document_processor import process_documents
from .vector_store import create_vector_store, query_vector_store
from .query_engine import QueryEngine

class ContentEngine:
    def __init__(self, data_directory):
        self.documents = process_documents(data_directory)
        self.vector_store = create_vector_store(self.documents)
        self.query_engine = QueryEngine()

    def answer_question(self, question):
        # Query the vector store
        relevant_docs = query_vector_store(self.vector_store, question)
        
        # Prepare context from relevant documents
        context = "\n".join([doc.page_content for doc in relevant_docs])
        
        # Generate answer using the query engine
        answer = self.query_engine.answer_question(question, context)
        
        return answer

if __name__ == "__main__":
    engine = ContentEngine("../data")
    question = "What are the main risk factors for these companies?"
    answer = engine.answer_question(question)
    print(answer)


__all__ = ['ContentEngine']