from openai import OpenAI
import os
from dotenv import load_dotenv
from .query_init import DatabaseHandler

class Agent:
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

    async def ask_ai(self, prompt: str, dialect: str) -> str:
        client = OpenAI(base_url=os.getenv("URL"), api_key=os.getenv("API_KEY"))
        response = client.chat.completions.create(
            model=os.getenv("AI_MODEL"),
            messages=[
                {"role": "system", "content": "Translate natural language to SQL."},
                {"role": "user", "content": prompt}
            ],
            stream=False
        )
        sql = response.choices[0].message.content.strip()
        return DatabaseHandler(dialect).run_query(sql)
