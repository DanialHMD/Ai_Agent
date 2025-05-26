from openai import OpenAI
import os
from dotenv import load_dotenv

class agent():
    def __init__(self):
        load_dotenv("/app")
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


    def build_prompt(dialect: str, user_prompt: str, mode: str, schema: str) -> str:
        return f"""
        # SQL Dialect: {dialect}
        # Mode: {mode}
        # Schema:
        {schema}
        # User Prompt:
        {user_prompt}
        """

    def ask_ai(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are an AI SQL assistant. Your task is to make queries with user given information."},
                {"role": "user", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"]