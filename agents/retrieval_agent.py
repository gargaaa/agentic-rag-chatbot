from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import torch

class RetrievalAgent:
    def __init__(self):
        # FORCE model to run on CPU ONLY
        torch_device = "cpu"
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.model.to(torch_device)  # manually override
        # This avoids meta tensor copying error

    def embed_texts(self, texts):
        return self.model.encode(texts, convert_to_tensor=True)

    def retrieve(self, query, documents, top_k=3):
        query_embedding = self.embed_texts([query])[0]
        doc_embeddings = self.embed_texts(documents)

        # Compute cosine similarities
        similarities = cosine_similarity(
            query_embedding.cpu().numpy().reshape(1, -1),
            [emb.cpu().numpy() for emb in doc_embeddings]
        )[0]

        # Get top-k relevant documents
        top_indices = np.argsort(similarities)[::-1][:top_k]
        return [documents[i] for i in top_indices]
