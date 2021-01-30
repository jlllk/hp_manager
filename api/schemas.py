from datetime import datetime

from typing import List, Optional

from pydantic import BaseModel, Field


class SessionCreate(BaseModel):
    pass


class Session(BaseModel):
    id: int
    deposit: int
    cash_out: int
    owner_id: int
    game_id: int

    class Config:
        orm_mode = True


class GameBase(BaseModel):
    title: str


class Game(GameBase):
    id: int
    timestamp: datetime
    sessions: Optional[List[Session]] = []

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str


class User(UserBase):
    id: int
    balance: int
    sessions: Optional[List[Session]] = []

    class Config:
        orm_mode = True


class Balance(BaseModel):
    balance: int
    reset: bool = Field(default=False)
