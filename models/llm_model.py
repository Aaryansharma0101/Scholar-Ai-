# models/llm_model.py
import os
from groq import Groq
import os

class LLMModel:
    def __init__(self):
        print("Loading Groq LLM...")

        # 🔑 Set your API key here or use env variable
        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )
    def generate(self, prompt, max_tokens=300):

        response = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",  # 🔥 best balance
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert AI research assistant. Be clear, structured, and accurate."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=max_tokens,
            temperature=0.2
        )

        return response.choices[0].message.content.strip()