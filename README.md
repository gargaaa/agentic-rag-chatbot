# Agentic RAG Chatbot

A Streamlit app that performs Retrieval-Augmented Generation (RAG) over uploaded documents using a retrieval agent.

## 📁 Supported File Types

- PDF
- DOCX
- PPTX
- CSV
- Markdown / TXT

## 💡 How It Works

1. Upload a file.
2. Extracts text using format-specific parsers.
3. (Planned) RAG agent performs retrieval and answers user queries.

## 🛠 Tech Stack

- Streamlit
- Sentence Transformers
- PyTorch
- OpenAI API
- FAISS or ChromaDB (for vector search)
- File parsing libs: PyMuPDF, python-docx, python-pptx, pandas, markdown2

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
