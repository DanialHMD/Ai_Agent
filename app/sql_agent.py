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
        client = OpenAI(base_url=os.getenv("URL"), api_key=os.getenv("API-KEY"))
        response = client.chat.completions.create(
            model=os.getenv("AI-MODEL"),
            messages=[
                {"role": "system", "content": "Your job is to translate natural language into SQL queries. Be precise and return only the SQL."},
                {"role": "user", "content": prompt},
            ],
            stream=False
        )

        return response.choices[0].message.content