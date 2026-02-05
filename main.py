from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/")
async def hackathon_entry(request: Request):
    body = await request.json()

    # message text jo scammer bhejta hai
    text = body["message"]["text"]

    # simple dummy reply (baad me smart bana lena)
    return {
        "status": "success",
        "reply": "Why is my account being suspended?"
    }
