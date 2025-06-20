from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pathlib import Path
from app.utils.sql_agent import Agent

SCHEMA = Path("app/utils/data.sql").read_text()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def serve_index() -> FileResponse:
    index_path = Path(__file__).parent / "static" / "index.html"
    return FileResponse(index_path)

# Mount static files like CSS/JS under /static/
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# API route
class QueryRequest(BaseModel):
    dialect: str
    prompt: str
    mode: str
    schema: str|None

@app.post("/api/sql-agent")
async def handle_prompt(request: QueryRequest) -> dict:
    prompt = await Agent().build_prompt(request.dialect, request.prompt, request.mode, SCHEMA)
    response = await Agent().ask_ai(prompt=prompt, dialect=request.dialect)
    return {"response": f"{response}"}