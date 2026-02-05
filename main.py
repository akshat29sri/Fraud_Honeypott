from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def root():
    return {"msg": "API live"}

@app.post("/")
async def receive(request: Request):
    body = await request.json()
    return {
        "status": "success",
        "reply": body["message"]["text"]
    }
