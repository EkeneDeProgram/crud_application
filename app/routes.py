from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .models import Book
from .db import get_db
from .schemas import BookCreate, BookUpdate, BookInDB
from pydantic import ValidationError
from typing import List
from sqlalchemy.orm import Mapper

router = APIRouter()


# Get endpoint to retrieve a list of all books.
@router.get("/books", response_model=List[BookInDB])
def read_books(db: Session = Depends(get_db)) -> List[BookInDB]:
    books = db.query(Book).all()
    return [BookInDB(**book.__dict__) for book in books]


# Get endpoint to retrieve information about a specific book.
@router.get("/books/{book_id}", response_model=BookInDB)
def read_book(book_id: str, db: Session = Depends(get_db)):
    try:
        book_id_int = int(book_id)
    except ValueError:
        # Handle the case where book_id is not a valid integer
        raise HTTPException(
            status_code=422, detail="Invalid book ID: must be an integer"
        )

    db_book = db.query(Book).filter(Book.id == book_id_int).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    # Convert the SQLAlchemy model instance to a dictionary
    if isinstance(db_book, Mapper):
        db_book = db_book.as_dict()

    # Convert the dictionary to a Pydantic model instance
    return BookInDB.from_orm(db_book)


# Post endpoint to add a new book to the collection.
@router.post("/books", response_model=BookInDB)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    try:
        # db_book = Book(**book.dict())
        db_book = Book(**dict(book))
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        return db_book
    except ValidationError as e:
        # Handle Pydantic validation errors
        raise HTTPException(status_code=422, detail=str(e))


# Put endpoint to update information about a specific book.
@router.put("/books/{book_id}", response_model=BookInDB)
def update_book(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    try:
        db_book = db.query(Book).filter(Book.id == book_id).first()
        if db_book is None:
            raise HTTPException(status_code=404, detail="Book not found")

        # for key, value in book.dict().items():
        for key, value in dict(book).items():
            # Only update non-None fields from the BookUpdate instance
            if value is not None:
                setattr(db_book, key, value)

        db.commit()
        db.refresh(db_book)
        return db_book

    except ValidationError as e:
        # Handle Pydantic validation errors
        raise HTTPException(status_code=422, detail=str(e))


# Delete endpoint to delete a book from the collection.
@router.delete("/books/{book_id}", response_model=BookInDB)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(db_book)
    db.commit()
    return db_book

