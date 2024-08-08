from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import models, schemas, crud, auth
from app.database import get_db

router = APIRouter()


@router.post("/books/{book_id}/reviews", response_model=schemas.Review)
def add_review(book_id: int, review: schemas.ReviewCreate, db: Session = Depends(get_db),
               token: str = Depends(auth.oauth2_scheme)):
    user_email = auth.verify_token(token)["sub"]
    user = crud.get_user_by_email(db, user_email)
    db_review = models.Review(user_id=user.id, book_id=book_id, rating=review.rating, comment=review.comment)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review


@router.get("/books/{book_id}/reviews", response_model=List[schemas.Review])
def get_reviews(book_id: int, db: Session = Depends(get_db)):
    return db.query(models.Review).filter(models.Review.book_id == book_id).all()
