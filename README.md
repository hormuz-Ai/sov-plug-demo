# Sovereignty Plug – Data Border Demo

Live API that enforces South African data residency (POPIA).

**Live Demo:** https://urban-space-barnacle-77999grwrx5whpj67-8001.app.github.dev/

**POST** `/check`
- `{"destination_country":"US"}` → `{"decision":"BLOCKED"}`
- `{"destination_country":"ZA"}` → `{"decision":"ALLOWED"}`

Built to prove POPIA compliance for Liquid C2 and African financial services.

## Run it
```bash
pip install fastapi uvicorn
uvicorn api:app --host 0.0.0.0 --port 8001