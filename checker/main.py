from fastapi import FastAPI

app = FastAPI()

@app.post("/check")
def read_root():
    return {"Hello": "World"}

@app.get("/check")
def readq_root():
    return {"Hello": "World"}