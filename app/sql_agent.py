from openai import OpenAI
import os
from dotenv import load_dotenv

class Agent():
    def __init__(self):
        load_dotenv()    

    async def build_prompt(self, dialect: str, user_prompt: str, mode: str, schema: str) -> str:
        return f"""
        # SQL Dialect: {dialect}
        # Mode: {mode}
        # Schema:
        {schema}
        # User Prompt:
        {user_prompt}
        """

    async def ask_ai(self, prompt: str) -> str:
        client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key="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")
        response = client.chat.completions.create(
            model="deepseek/deepseek-r1:free",
            messages=[
                {"role": "system", "content": "Your job is to translate natural language into SQL queries. Be precise and return only the SQL."},
                {"role": "user", "content": prompt},
            ],
            stream=False
        )

        return response.choices[0].message.content