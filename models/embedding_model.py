from sentence_transformers import SentenceTransformer

class EmbeddingModel:
    def __init__(self):
        device = "cpu"  # ✅ force CPU for deployment
        print(f"Using device for embeddings: {device}")

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2",
            device=device
        )

    def encode(self, texts):
        return self.model.encode(texts, convert_to_numpy=True)
