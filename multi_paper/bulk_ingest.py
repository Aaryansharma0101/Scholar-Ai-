# multi_paper/ingest.py

from deep_reader.parser import extract_text, extract_abstract
from models.embedding_model import EmbeddingModel
from deep_reader.vector_store import VectorStore

class MultiPaperEngine:
    def __init__(self):
        self.embedding_model = EmbeddingModel()
        self.vector_store = None
        self.metadata = []

    def ingest_papers(self, uploaded_files):

        texts = []
        abstracts = []

        for file in uploaded_files:
            text = extract_text(file)
            abstract = extract_abstract(text)

            texts.append(text)
            abstracts.append(abstract)

            self.metadata.append({
                "filename": file.name,
                "abstract": abstract
            })

        embeddings = self.embedding_model.encode(abstracts)

        dimension = embeddings.shape[1]
        self.vector_store = VectorStore(dimension)
        self.vector_store.add(embeddings, abstracts)

        return "Papers indexed successfully"