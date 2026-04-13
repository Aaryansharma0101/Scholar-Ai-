# deep_reader/parser.py

import fitz  # PyMuPDF

def extract_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_abstract(text):
    """
    Extracts abstract section from research paper text.
    Falls back to first 1500 chars if not found.
    """

    lower_text = text.lower()

    start = lower_text.find("abstract")
    end = lower_text.find("introduction")

    if start != -1 and end != -1 and end > start:
        return text[start:end]

    # fallback
    return text[:1500]