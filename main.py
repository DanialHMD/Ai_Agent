from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pathlib import Path
from app.sql_agent import agent

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
    prompt = agent().build_prompt(request.dialect, request.prompt, request.mode, SCHEMA)
    response = agent().ask_ai(prompt=prompt)
    return {"response": f"Received: {request.dialect}, {request.mode}, {request.prompt}"}
