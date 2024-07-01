# src/document_processor.py

import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def process_documents(directory):
    documents = {}
    for filename in os.listdir(directory):
        if filename.endswith('.pdf'):
            file_path = os.path.join(directory, filename)
            company_name = filename.split('_')[0].capitalize()
            
            # Load PDF
            loader = PyPDFLoader(file_path)
            pages = loader.load()
            
            # Split text into chunks
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200,
                length_function=len
            )
            chunks = text_splitter.split_documents(pages)
            
            documents[company_name] = chunks
    
    return documents

if __name__ == "__main__":
    data_directory = "../data"
    processed_docs = process_documents(data_directory)
    for company, chunks in processed_docs.items():
        print(f"{company}: {len(chunks)} chunks")