import streamlit as st
import uuid
import os
from agents.ingestion_agent import IngestionAgent
from agents.retrieval_agent import RetrievalAgent
from agents.llm_response_agent import LLMResponseAgent

st.set_page_config(page_title="Agentic RAG Chatbot", layout="wide")
st.title("🤖 Agentic RAG Chatbot")
st.markdown("Upload documents (PDF, DOCX, PPTX, CSV, TXT/Markdown) and ask questions!")

uploaded_files = st.file_uploader("📁 Upload your files", accept_multiple_files=True)
query = st.text_input("❓ Ask a question about the documents")

if uploaded_files and query:
    trace_id = str(uuid.uuid4())
    ingestion = IngestionAgent()
    retrieval = RetrievalAgent()
    llm = LLMResponseAgent()
    if not os.path.exists("data"):
     os.makedirs("data")
    file_paths = []
    for f in uploaded_files:
        path = f"data/{f.name}"
        with open(path, "wb") as out:
            out.write(f.read())
        file_paths.append(path)

    doc_msg = ingestion.run(file_paths, trace_id)
    retrieval.index_docs(doc_msg["payload"]["docs"])
    retr_msg = retrieval.retrieve(query, trace_id)
    llm_msg = llm.run(retr_msg["payload"], trace_id)

    st.subheader("💬 Answer")
    st.success(llm_msg["payload"]["answer"])

    st.subheader("📚 Retrieved Context")
    for chunk in retr_msg["payload"]["retrieved_context"]:
        st.markdown(f"> {chunk}")
