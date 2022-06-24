from typing import Optional
from pydantic import BaseModel
# from uuid import UUID, uuid4


class User(BaseModel):
    id: int
    name: str
    balance: int


class SendMoney(BaseModel):
    balance: int
