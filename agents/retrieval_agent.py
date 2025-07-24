from sentence_transformers import SentenceTransformer
from utils.mcp import create_message
import faiss
import numpy as np
import torch

class RetrievalAgent:
    def __init__(self):
        device = 'cpu'
        torch_device = torch.device(device)
        self.model = SentenceTransformer('all-MiniLM-L6-v2', device=device)
        self.model.to(torch_device)
        self.index = faiss.IndexFlatL2(384)
        self.docs = []

    def index_docs(self, docs):
        embeddings = self.model.encode(docs)
        self.index.add(np.array(embeddings))
        self.docs = docs

    def retrieve(self, query, trace_id):
        query_emb = self.model.encode([query])
        D, I = self.index.search(np.array(query_emb), 3)
        top_chunks = [self.docs[i] for i in I[0]]
        return create_message(
            sender="RetrievalAgent",
            receiver="LLMResponseAgent",
            type_="RETRIEVAL_RESULT",
            payload={"retrieved_context": top_chunks, "query": query},
            trace_id=trace_id
        )
