from fastapi import APIRouter, Query, HTTPException
from typing import Optional
from .service import search_players
from .schemas import PlayerList

router = APIRouter()


@router.get("/players", response_model=PlayerList)
async def get_players(
    name: Optional[str] = Query(None, description="部分一致検索: 名前"),
    country: Optional[str] = Query(None, description="国名（完全一致、case-insensitive）"),
    position: Optional[str] = Query(None, description="ポジション（例: MF, FW）"),
    min_height: Optional[int] = Query(None, ge=0, description="最小身長(cm)"),
    max_height: Optional[int] = Query(None, ge=0, description="最大身長(cm)"),
    min_age: Optional[int] = Query(None, ge=0, description="最小年齢"),
    max_age: Optional[int] = Query(None, ge=0, description="最大年齢"),
    offset: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
):
    try:
        players, total = await search_players(
            name=name,
            country=country,
            position=position,
            min_height=min_height,
            max_height=max_height,
            min_age=min_age,
            max_age=max_age,
            offset=offset,
            limit=limit,
        )
        return PlayerList(players=players, total=total)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
