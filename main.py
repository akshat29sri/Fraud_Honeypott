from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from api import analyze_text

app = FastAPI()

API_KEY = "honeypot-hackathon-2026-secret"

class Message(BaseModel):
    sender: str
    text: str
    timestamp: int

class RequestBody(BaseModel):
    sessionId: str
    message: Message
    conversationHistory: list
    metadata: dict

@app.get("/")
def root():
    return {"msg": "API live"}

@app.post("/")
def analyze(payload: RequestBody, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")

    reply = analyze_text(payload.message.text)

    return {
        "status": "success",
        "reply": reply
    }
