from typing import Optional

from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str
    password: str


class User(BaseModel):
    id: int
    email: str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
