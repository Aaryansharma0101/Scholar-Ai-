class StructuredSummarizer:
    def __init__(self, llm):
        self.llm = llm

    def extract_structure(self, text):

        short_text = text[:1500]

        prompt = f"""
Summarize the following research paper in a clear and detailed paragraph.

Include:
- What problem the paper solves
- What method is used
- Key results
- Main contribution

Write it as a well-structured paragraph (NOT JSON).

Paper:
{text[:3000]}
"""

        response = self.llm.generate(prompt, max_tokens=200)

        print("MODEL OUTPUT:", response)

        return {"problem_statement": response}