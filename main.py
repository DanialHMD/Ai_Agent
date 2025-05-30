from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pathlib import Path
from app.sql_agent import Agent
import sqlite3
import psycopg2
import mysql.connector
from app.utils.query_init import DatabaseHandler

SCHEMA = Path("app/schema.sql").read_text()
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def serve_index():
    index_path = Path(__file__).parent / "app" / "static" / "index.html"
    return FileResponse(index_path)

# Mount static files like CSS/JS under /static/
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# API route
class QueryRequest(BaseModel):
    dialect: str
    prompt: str
    mode: str

@app.post("/api/sql-agent")
async def handle_prompt(request: QueryRequest):
    prompt = await Agent().build_prompt(request.dialect, request.prompt, request.mode, SCHEMA)
    response = await Agent().ask_ai(prompt=prompt)
    return {"response": f"{response}"}



def get_connection(dialect):
    if dialect == "sqlite":
        return sqlite3.connect("my.db")
    elif dialect == "postgresql":
        return psycopg2.connect(
            dbname="mydb", user="postgres", password="pass", host="localhost", port=5432
        )
    elif dialect == "mysql":
        return mysql.connector.connect(
            host="localhost", user="root", password="pass", database="mydb"
        )
    else:
        raise ValueError("Unsupported dialect")

def get_query():
    return "SELECT * FROM users"

def main():
    dialect = input("Enter SQL dialect (sqlite/postgresql/mysql): ").strip().lower()
    connection = get_connection(dialect)
    db = DatabaseHandler(dialect, connection)

    query = get_query()
    results = db.run_query(query)

    print(results)
    connection.close()

if __name__ == "__main__":
    main()
