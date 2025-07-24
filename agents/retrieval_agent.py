from sentence_transformers import SentenceTransformer
import torch

class RetrievalAgent:
    def __init__(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Using device: {device}")
        self.model = SentenceTransformer("all-MiniLM-L6-v2", device=device)

    def embed(self, texts):
        return self.model.encode(texts, convert_to_tensor=True)
