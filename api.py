from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI(title="Sovereignty Plug - Data Border")

@app.post("/check")
async def check(req: Request):
    data = await req.json()
    dest = data.get("destination_country", "")
    if dest != "ZA":
        return JSONResponse({"decision": "BLOCKED", "reason": f"Data residency violation: {dest}"})
    return JSONResponse({"decision": "ALLOWED", "reason": "Within South Africa"})

@app.get("/")
def root():
    return {"status": "Border active. POST to /check"}
