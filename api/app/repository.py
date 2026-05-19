import json
import asyncio
from pathlib import Path
from typing import List, Optional

_DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "players.json"
_cache: Optional[List[dict]] = None
_cache_lock = asyncio.Lock()


async def load_all_players() -> List[dict]:
    """Load players from JSON file and cache in memory."""
    global _cache
    if _cache is not None:
        return _cache
    async with _cache_lock:
        if _cache is not None:
            return _cache
        text = _DATA_PATH.read_text(encoding="utf-8")
        data = json.loads(text)
        _cache = data
        assert _cache is not None
        return _cache
