# Sovereignty Plug – Data Border Demo

Live API that enforces South African data residency (POPIA).

**Live Demo:** https://sov-plug-demo.onrender.com/docs

**POST** `/check`
- `{"destination_country":"US"}` → `{"decision":"BLOCKED"}`
- `{"destination_country":"ZA"}` → `{"decision":"ALLOWED"}`

Built to prove POPIA compliance for Liquid C2 and African financial services.

## Run it
```bash
pip install fastapi uvicorn
uvicorn api:app --host 0.0.0.0 --port 8001