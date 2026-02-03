from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .ai import ask_gemini
from .rate_limit import rate_limit

app = FastAPI(title="F-Planner AI API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Prompt(BaseModel):
    prompt: str

@app.get("/")
def root():
    return {"status": "online"}

@app.post("/ask")
def ask(prompt: Prompt, request: Request):
    rate_limit(request)
    return {"response": ask_gemini(prompt.prompt)}
