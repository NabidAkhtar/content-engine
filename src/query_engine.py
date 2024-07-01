# src/query_engine.py
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_huggingface import HuggingFacePipeline
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

class QueryEngine:
    def __init__(self):
        model_name = "gpt2"  # You can use a larger model if your system can handle it
        model = AutoModelForCausalLM.from_pretrained(model_name)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, max_length=1000)
        self.llm = HuggingFacePipeline(pipeline=pipe)

        self.template = """
        Question: {question}
        Context: {context}
        Answer: Let's approach this step-by-step:
        1)
        """
        self.prompt = PromptTemplate(template=self.template, input_variables=["question", "context"])
        self.chain = (
            {"question": RunnablePassthrough(), "context": RunnablePassthrough()}
            | self.prompt
            | self.llm
            | StrOutputParser()
        )

    def answer_question(self, question, context):
        return self.chain.invoke({"question": question, "context": context})

def generate_comparison(query_engine, documents, question):
    comparison = f"Comparison for the question: '{question}'\n\n"
    for company, docs in documents.items():
        context = "\n".join([doc.page_content for doc in docs[:2]])  # Use first 2 chunks for context
        response = query_engine.answer_question(question, context)
        comparison += f"{company}:\n{response}\n\n"
    
    return comparison

if __name__ == "__main__":
    # Test the query engine
    from document_processor import process_documents
    
    data_directory = "../data"
    processed_docs = process_documents(data_directory)
    query_engine = QueryEngine()
    comparison = generate_comparison(query_engine, processed_docs, "What are the main risk factors?")
    print(comparison)