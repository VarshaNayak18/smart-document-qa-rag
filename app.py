import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

from src.loader import load_pdf
from src.splitter import split_documents
from src.embeddings import create_vector_store
from src.qa_chain import create_qa_chain

st.set_page_config(page_title="Smart Document Q&A")

st.title("📄 Smart Document Q&A (RAG)")
st.write("Upload a PDF and ask questions!")

# Upload PDF
uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_file:
    import tempfile
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        file_path = tmp_file.name

    st.success("PDF uploaded successfully!")

    with st.spinner("Processing document..."):
        docs = load_pdf(file_path)
        chunks = split_documents(docs)
        vectorstore = create_vector_store(chunks)
        qa_chain = create_qa_chain(vectorstore)

    st.success("Ready! Ask your question 👇")

    query = st.text_input("Enter your question:")

    if query:
        with st.spinner("Thinking..."):
            response = qa_chain(query)
            st.write("### 📌 Answer:")
            st.write(response)