### **Context and scope**

This project, named "Content Engine", is a question-answering system designed to process and analyze company documents (specifically PDF files) and provide answers to user queries about these companies. The system uses natural language processing and vector storage techniques to efficiently retrieve relevant information and generate responses.

The main components of the system include:

Document processing

Vector store creation and querying

Query engine for generating answers

A Streamlit-based user interface

The system is designed to work with PDF documents stored in a specific directory, process them, create a searchable vector store, and then use this store along with a language model to answer user questions.

### **Goals and non-goals**

Goals:

Process and analyze company documents (PDFs) efficiently

Create a searchable vector store of document content

Generate relevant answers to user queries about the companies

Provide a user-friendly interface for asking questions and receiving answers

Non-goals:

Real-time document processing or updating

Handling document formats other than PDF

Automated data collection or web scraping of company information

Providing financial advice or recommendations based on the analyzed data


![Screenshot 2024-07-01 183734](https://github.com/NabidAkhtar/content-engine/assets/136959977/39b4cf9e-50d6-4b09-9c53-7d9a4370c1b0)



### **API**

The main API for this system is the ContentEngine class in src/main.py:

 
    class ContentEngine:
      def __init__(self, data_directory):
        # Initialize the engine with a data directory

      def answer_question(self, question):
        # Process a question and return an answer

This API is used by the Streamlit UI to interact with the underlying system.

### **Data storage**

The system uses two main forms of data storage:

Document chunks: Processed documents are split into chunks and stored in memory as a dictionary, with company names as keys and lists of document chunks as values.

Vector store: Document chunks are converted into vector representations and stored in a Chroma vector store. This has persisted on disk in the ./chroma_db directory.

### **Code and pseudo-code**

The main workflow of the system can be described as follows:

Process documents:

Load PDF files from the data directory

Split documents into chunks

Store chunks in a dictionary

Create vector store:

Convert document chunks to vector representations

Store vectors in a Chroma database

Answer questions:

Receive a question from the user

Query the vector store for relevant document chunks

Use the query engine to generate an answer based on the question and relevant context

### **Degree of constraint**

This system operates under moderate constraints:

It is designed to work specifically with PDF documents

It uses pre-trained models for embeddings and language processing

The vector store implementation is tied to the Chroma database

The user interface is built using Streamlit

These constraints provide a clear structure for the system but still allow for flexibility in terms of the specific models used and the types of questions that can be answered.

### **Alternatives considered**

Using a different vector store:

Alternative: Pinecone or Faiss

Trade-off: Chroma was chosen for its simplicity and easy integration with local storage. Pinecone would require cloud deployment, and Faiss might be more complex to set up.

Using a different language model:

Alternative: OpenAI's GPT models

Trade-off: The current implementation uses HuggingFace models, which can be run locally and are open-source. OpenAI's models might provide better results but would require API calls and associated costs.

Implementing a web scraping component:

Alternative: Automatically collect company information from the web

Trade-off: This would increase the complexity of the system and might introduce legal and ethical concerns. The current approach of using pre-existing PDF documents is simpler and more controlled.

Using a different UI framework:

Alternative: Flask or Django web application

Trade-off: Streamlit was chosen for its simplicity and rapid prototyping capabilities. A more traditional web framework would offer more customization but require more development time.
