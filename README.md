# Sovereignty Plug – Data Border Demo

Live API that enforces South African data residency.

**POST** `/check`
- `{"destination_country":"US"}` → `{"decision":"BLOCKED"}`
- `{"destination_country":"ZA"}` → `{"decision":"ALLOWED"}`

Built in 3 hours to prove POPIA compliance for Liquid C2 and African banks.

## Run it
```bash
13  pip install fastapi uvicorn
14  uvicorn api:app --port 8000
```
