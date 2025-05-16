from pathlib import Path
import openai
import os

SCHEMA_PATH = Path("schema.sql")
openai.api_key = os.getenv("DEEPSEEK_API_KEY")

def load_schema():
    return SCHEMA_PATH.read_text()

def build_prompt(dialect: str, user_prompt: str, mode: str, schema: str):
    return f"""
    # SQL Dialect: {dialect}
    # Mode: {mode}
    # Schema:
    {schema}
    # User Prompt:
    {user_prompt}
    """

def ask_openai(prompt: str) -> str:
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]
