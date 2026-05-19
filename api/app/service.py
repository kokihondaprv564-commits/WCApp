from typing import List, Optional, Tuple
from .repository import load_all_players
from .schemas import Player


async def search_players(
    name: Optional[str] = None,
    country: Optional[str] = None,
    club: Optional[str] = None,
    position: Optional[str] = None,
    min_height: Optional[int] = None,
    max_height: Optional[int] = None,
    min_age: Optional[int] = None,
    max_age: Optional[int] = None,
    offset: int = 0,
    limit: int = 100,
) -> Tuple[List[Player], int]:
    """Return list of players matching optional filters."""
    data = await load_all_players()
    results: List[dict] = []

    for p in data:
        if name:
            if name.lower() not in p.get("name", "").lower():
                continue
        if country:
            if country.lower() != p.get("country", "").lower():
                continue
        if club:
            if club.lower() not in p.get("club", "").lower():
                continue
        if position:
            if position.lower() != p.get("position", "").lower():
                continue
        if min_height is not None:
            if p.get("height_cm") is None or p["height_cm"] < min_height:
                continue
        if max_height is not None:
            if p.get("height_cm") is None or p["height_cm"] > max_height:
                continue
        if min_age is not None:
            if p.get("age") is None or p["age"] < min_age:
                continue
        if max_age is not None:
            if p.get("age") is None or p["age"] > max_age:
                continue

        results.append(p)

    sliced = results[offset : offset + limit]
    return [Player(**r) for r in sliced], len(results)
