from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

print("server running")


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.mount("/", StaticFiles(directory="app/static", html=True), name="static")

class QueryRequest(BaseModel):
    dialect: str
    prompt: str
    mode: str

@app.post("/api/sql-agent")
async def handle_prompt(request: QueryRequest):
    return {"response": "OK"}
