from fastapi import FastAPI

from app import models
from app.database import engine
from app.routers import users, books, reviews, bookmarks

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(books.router)
app.include_router(reviews.router)
app.include_router(bookmarks.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Book Review App"}
