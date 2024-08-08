from fastapi import FastAPI

from app.routers import users

app = FastAPI()

app.include_router(users.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Book Review App"}
