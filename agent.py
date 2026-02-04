import re
import uuid
from datetime import datetime

SCAM_KEYWORDS = [
    "urgent", "blocked", "verify", "otp",
    "account", "transfer", "refund", "click"
]

def detect_scam(text: str) -> bool:
    return any(k in text.lower() for k in SCAM_KEYWORDS)

def extract_intel(text: str):
    return {
        "bank_accounts": re.findall(r"\b\d{9,18}\b", text),
        "upi_ids": re.findall(r"\b[\w.-]+@[\w.-]+\b", text),
        "phishing_links": re.findall(r"https?://\S+", text)
    }

class PersonaAgent:
    def respond(self, message: str) -> str:
        replies = [
            "I don’t understand, what do you mean?",
            "Is my money safe right now?",
            "Which account should I send it to?",
            "Can you send the official link again?",
            "UPI will work right?"
        ]
        return replies[len(message) % len(replies)]

class HoneypotAgent:
    def __init__(self):
        self.session_id = str(uuid.uuid4())
        self.persona = PersonaAgent()
        self.intelligence = {
            "bank_accounts": [],
            "upi_ids": [],
            "phishing_links": []
        }

    def handle_message(self, message: str):
        if not detect_scam(message):
            return None

        intel = extract_intel(message)
        for k in self.intelligence:
            self.intelligence[k].extend(intel[k])

        return self.persona.respond(message)

    def report(self):
        return {
            "session_id": self.session_id,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "threat": "Financial Scam",
            "intelligence": self.intelligence
        }
