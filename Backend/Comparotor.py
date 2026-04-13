# Backend/comparator.py

from models.llm_model import LLMModel

# 🔥 Load once (IMPORTANT)
llm_model = LLMModel()


def compare_papers(files):

    abstracts = []

    for file in files:

        # 🚀 ULTRA FAST METHOD (NO PDF PARSING)
        file.seek(0)
        text = file.read().decode(errors="ignore")[:1000]

        abstracts.append(text)

    # 🔥 Only compare 2 papers for speed + quality
    combined_text = "\n\n".join(abstracts[:2])

    prompt = f"""
Compare the following research papers in a table format.

| Feature | Paper 1 | Paper 2 |
|---------|--------|--------|
| Problem |        |        |
| Method  |        |        |
| Results |        |        |
| Strengths |      |        |
| Weaknesses |     |        |

Use short phrases.

Papers:
{combined_text}
"""

    return llm_model.generate(prompt, max_tokens=150)