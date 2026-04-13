# multi_paper/comparator.py

def compare_papers(llm, papers):

    combined_text = "\n\n".join(papers)

    prompt = f"""
Compare the following research papers.

Explain:
- Key differences
- Methods used
- Performance differences
- Which is better and why

Write in a clear structured explanation.

Papers:
{combined_text}
"""

    return llm.generate(prompt, max_tokens=400)