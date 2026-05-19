from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi import APIRouter
from fastapi.middleware.cors import CORSMiddleware

from .routes import router as players_router

app = FastAPI(title="WCApp API")

# 開発用に簡易的な CORS 設定を追加
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(players_router)
