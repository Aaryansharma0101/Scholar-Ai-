from sentence_transformers import SentenceTransformer
import torch

class EmbeddingModel:
    def __init__(self):
        device = "cuda"
        print(f"Using device for embeddings: {device}")
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.model = self.model.to(device)

    def encode(self, texts):
        return self.model.encode(texts, convert_to_numpy=True)