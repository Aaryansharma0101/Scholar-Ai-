# deep_reader/rag.py

class RAGEngine:
    def __init__(self, embedding_model, vector_store, llm):
        self.embedding_model = embedding_model
        self.vector_store = vector_store
        self.llm = llm

    def answer(self, question):
        query_embedding = self.embedding_model.encode([question])[0]
        relevant_chunks = self.vector_store.search(query_embedding)

        context = "\n\n".join(relevant_chunks)

        prompt = f"""
            Answer the question based only on the context below.

            Context:
            {context}

            Question:
            {question}

            Answer clearly and in 4-6 sentences.
            """

        return self.llm.generate(prompt)
    
