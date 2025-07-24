import streamlit as st
from agents.retrieval_agent import RetrievalAgent
from utils.file_loader import load_file

st.set_page_config(page_title="Agentic RAG Chatbot", layout="wide")

st.title("🤖 Agentic RAG Chatbot for Document QA")
uploaded_file = st.file_uploader("Upload a document (PDF, DOCX, PPTX, CSV, MD, TXT)", type=["pdf", "docx", "pptx", "csv", "md", "txt"])

if uploaded_file:
    with open(f"data/{uploaded_file.name}", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.success("File uploaded successfully!")
    file_path = f"data/{uploaded_file.name}"
    file_content = load_file(file_path)
    st.text_area("Extracted Text Preview", value=file_content[:3000], height=300)

    query = st.text_input("Ask your question about the document")
    if query:
        st.info("Retrieval and answer generation is not implemented here (mock demo).")
        # Add RAG logic or LLM response here.
