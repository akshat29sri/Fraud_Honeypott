from fastapi import FastAPI
from agent import HoneypotAgent
from mock_scammer import get_scammer_messages
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Agentic Scam Honeypot")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # hackathon ke liye OK
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

agent = HoneypotAgent()

@app.get("/")
def home():
    return {"status": "Agentic Honeypot Running"}

@app.get("/simulate")
def simulate_attack():
    conversation = []

    for msg in get_scammer_messages():
        reply = agent.handle_message(msg)
        conversation.append({
            "scammer": msg,
            "agent": reply
        })

    return {
        "conversation": conversation,
        "report": agent.report()
    }
