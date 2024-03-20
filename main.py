from fastapi import FastAPI
import requests
from pydantic import BaseModel

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str
    max_len: int = 100
    temperature: float = 0.01

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/generate/")
def read_item(prompt_request: PromptRequest):
    return {"Hello": requests.post("http://host.docker.internal:8000/generate", json={
        "prompt": prompt_request.prompt
    })}
