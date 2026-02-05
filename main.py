from fastapi import FastAPI, Header
from pydantic import BaseModel

app = FastAPI()

API_KEY = "honeypot-hackathon-2026-secret"

class IncomingMessage(BaseModel):
    sessionId: str
    message: dict
    conversationHistory: list
    metadata: dict


@app.post("/")
def hackathon_entry(payload: IncomingMessage, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        return {
            "status": "error",
            "reply": "Invalid API key"
        }

    scam_text = payload.message.get("text", "")

    # Simple honeypot reply logic
    reply = "Why is my account being suspended?"

    return {
        "status": "success",
        "reply": reply
    }
