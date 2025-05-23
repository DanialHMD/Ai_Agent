from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pathlib import Path

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Serve the HTML at root "/"
@app.get("/")
def serve_index():
    return FileResponse("app/static/index.html")

# Mount static files like CSS/JS under /static/
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# API route
class QueryRequest(BaseModel):
    dialect: str
    prompt: str
    mode: str

@app.post("/api/sql-agent")
async def handle_prompt(request: QueryRequest):
    return {"response": f"Received: {request.dialect}, {request.mode}, {request.prompt}"}
