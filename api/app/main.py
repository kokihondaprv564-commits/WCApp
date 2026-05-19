from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi import APIRouter

from .routes import router as players_router

app = FastAPI(title="WCApp API")


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(players_router)
