import openai
import os
from dotenv import load_dotenv

load_dotenv("/app")
openai.api_key = os.getenv("DEEPSEEK_API_KEY")

def build_prompt(dialect: str, user_prompt: str, mode: str, schema: str):
    return f"""
    # SQL Dialect: {dialect}
    # Mode: {mode}
    # Schema:
    {schema}
    # User Prompt:
    {user_prompt}
    """

def ask_ai(prompt: str) -> str:
    response = openai.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are an AI SQL assistant. Your task is to make queries with user given information."},
            {"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]
