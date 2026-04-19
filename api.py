from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.post("/check")
def check(body: dict):
    return {"decision": "BLOCKED" if body.get("destination_country")=="US" else "ALLOWED"}

@app.get("/")
def home():
    return FileResponse("dashboard.html")
