# Backend/Analyzer.py

import tempfile

from models.embedding_model import EmbeddingModel
from models.llm_model import LLMModel

from deep_reader.parser import extract_text
from deep_reader.chunker import chunk_text
from deep_reader.vector_store import VectorStore
from deep_reader.rag import RAGEngine
from deep_reader.summarizer import StructuredSummarizer


def process_pdf(uploaded_file):

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        pdf_path = tmp_file.name

    text = extract_text(pdf_path)
    chunks = chunk_text(text)

    embedding_model = EmbeddingModel()
    llm_model = LLMModel()

    embeddings = embedding_model.encode(chunks)
    dimension = embeddings.shape[1]

    vector_store = VectorStore(dimension)
    vector_store.add(embeddings, chunks)

    rag_engine = RAGEngine(embedding_model, vector_store, llm_model)
    summarizer = StructuredSummarizer(llm_model)

    return {
        "text": text,
        "rag": rag_engine,
        "summarizer": summarizer
    }


def generate_summary(text, summarizer):
    return summarizer.extract_structure(text)


def ask_question(question, rag_engine):
    return rag_engine.answer(question)