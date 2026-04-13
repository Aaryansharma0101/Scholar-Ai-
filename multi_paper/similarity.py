# multi_paper/similarity.py

def find_similar(engine, query_text, top_k=3):

    query_embedding = engine.embedding_model.encode([query_text])[0]
    results = engine.vector_store.search(query_embedding, k=top_k)

    return results