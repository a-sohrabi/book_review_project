from typing import Optional, List

from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str
    password: str


class User(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


class BookCreate(BaseModel):
    title: str
    summary: str


class Book(BaseModel):
    id: int
    title: str
    summary: str

    class Config:
        from_attributes = True


class BookDetail(Book):
    bookmark_count: int
    reviews: List['Review'] = []


class ReviewCreate(BaseModel):
    rating: int
    comment: Optional[str] = None


class Review(BaseModel):
    id: int
    rating: int
    comment: str
    user_id: int
    book_id: int

    class Config:
        from_attributes = True


class Bookmark(BaseModel):
    id: int
    user_id: int
    book_id: int

    class Config:
        from_attributes = True
