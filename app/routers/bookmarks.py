from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import models, schemas, crud, auth
from app.database import get_db

router = APIRouter()


@router.post("/books/{book_id}/bookmark", response_model=schemas.Bookmark)
def bookmark_book(book_id: int, db: Session = Depends(get_db), token: str = Depends(auth.oauth2_scheme)):
    token_data = auth.verify_token(token)
    if token_data is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    user_email = token_data.get("sub")
    user = crud.get_user_by_email(db, user_email)
    if db.query(models.Review).filter(models.Review.book_id == book_id, models.Review.user_id == user.id).first():
        raise HTTPException(status_code=400, detail="Cannot bookmark a book you've reviewed")
    db_bookmark = models.Bookmark(user_id=user.id, book_id=book_id)
    db.add(db_bookmark)
    db.commit()
    db.refresh(db_bookmark)
    return db_bookmark


@router.delete("/books/{book_id}/bookmark", status_code=status.HTTP_204_NO_CONTENT)
def remove_bookmark(book_id: int, db: Session = Depends(get_db), token: str = Depends(auth.oauth2_scheme)):
    user_email = auth.verify_token(token)["sub"]
    user = crud.get_user_by_email(db, user_email)
    bookmark = db.query(models.Bookmark).filter(models.Bookmark.book_id == book_id,
                                                models.Bookmark.user_id == user.id).first()
    if not bookmark:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    db.delete(bookmark)
    db.commit()
    return
