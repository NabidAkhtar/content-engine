# app.py

import streamlit as st
from src.main import ContentEngine

def main():
    st.title("Content Engine")

    # Initialize ContentEngine
    engine = ContentEngine("data")

    # User input
    question = st.text_input("Enter your question about the companies:")

    if st.button("Get Answer"):
        if question:
            with st.spinner("Analyzing documents..."):
                answer = engine.answer_question(question)
            st.write(answer)
        else:
            st.warning("Please enter a question.")

if __name__ == "__main__":
    main()