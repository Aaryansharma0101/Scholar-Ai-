# Backend/similarity.py

from models.embedding_model import EmbeddingModel
from deep_reader.vector_store import VectorStore
from deep_reader.parser import extract_abstract

embedding_model = EmbeddingModel()

# Temporary in-memory storage (can upgrade later)
stored_abstracts = []
stored_embeddings = None
vector_store = None


def add_paper(text):

    global stored_embeddings, vector_store

    abstract = extract_abstract(text)

    embedding = embedding_model.encode([abstract])

    stored_abstracts.append(abstract)

    if stored_embeddings is None:
        stored_embeddings = embedding
    else:
        import numpy as np
        stored_embeddings = np.vstack([stored_embeddings, embedding])

    dimension = stored_embeddings.shape[1]
    vector_store = VectorStore(dimension)
    vector_store.add(stored_embeddings, stored_abstracts)


def find_similar(text, top_k=3):

    if vector_store is None:
        return ["No papers indexed yet"]

    query = extract_abstract(text)
    query_embedding = embedding_model.encode([query])[0]

    results = vector_store.search(query_embedding, k=top_k)

    return results