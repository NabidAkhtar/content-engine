# src/vector_store.py

from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import os

def create_vector_store(documents):
    # Initialize the embedding function
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    # Check if the vector store already exists
    if os.path.exists("./chroma_db"):
        # Load existing vector store
        vector_store = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
    else:
        # Create a new Chroma vector store
        vector_store = Chroma.from_documents(
            documents=[doc for company_docs in documents.values() for doc in company_docs],
            embedding=embeddings,
            persist_directory="./chroma_db"
        )
        vector_store.persist()  # Persist the vector store to disk
    return vector_store

def query_vector_store(vector_store, query, k=4):
    results = vector_store.similarity_search(query, k=k)
    return results

if __name__ == "__main__":
    # Test the vector store
    from document_processor import process_documents
    
    data_directory = "../data"
    processed_docs = process_documents(data_directory)
    vector_store = create_vector_store(processed_docs)
    
    query_results = query_vector_store(vector_store, "What are the main risk factors?")
    for doc in query_results:
        print(doc.page_content[:100] + "...\n")