from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json
from pathlib import Path

app = FastAPI(title="WCApp API")

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "players.json"


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/players")
async def list_players():
    try:
        data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
        return JSONResponse(content=data)
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
