# Sovereignty Plug – Data Border Demo

Live API that enforces South African data residency.

**POST** /check
{"destination_country":"US"} → {"decision":"BLOCKED"}
{"destination_country":"ZA"} → {"decision":"ALLOWED"}

Built in 3 hours to prove POPIA compliance for Liquid C2 and African banks.
## Run it
pip install fastapi uvicorn
uvicorn api:app --port 8000
curl -X POST http://localhost:8000/check -d '{"destination_country":"US"}' -H "Content-Type: application/json"