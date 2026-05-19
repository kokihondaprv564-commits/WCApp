from pydantic import BaseModel
from typing import List


class Player(BaseModel):
    id: int
    name: str
    country: str
    position: str
    height_cm: int
    age: int


class PlayerList(BaseModel):
    players: List[Player]
    total: int
