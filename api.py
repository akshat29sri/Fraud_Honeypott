from fastapi import FastAPI
import main

app = FastAPI()

@app.get("/")
def root():
    return {"msg": "API live"}

@app.get("/run")
def run_code():
    return {"result": "logic executed"}
