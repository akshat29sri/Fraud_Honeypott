from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

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

@app.post("/analyze")
def analyze(payload: RequestBody, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")

    text = payload.message.text.lower()

    if "bank" in text or "verify" in text or "blocked" in text:
        reply = "This looks like a scam. Do not click any links."
    else:
        reply = "Message seems safe."

    return {
        "status": "success",
        "reply": reply
    }
