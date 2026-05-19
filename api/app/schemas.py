from pydantic import BaseModel
from typing import List


class Player(BaseModel):
    id: int
    name: str
    country: str
    club: str
    position: str
    height_cm: int
    age: int
    # 2025/2026 season statistics
    goals: int = 0
    assists: int = 0
    clean_sheets: int = 0
    yellow_cards: int = 0
    red_cards: int = 0


class PlayerList(BaseModel):
    players: List[Player]
    total: int
