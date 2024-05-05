from typing import Optional
from pydantic import BaseModel


# Schema for a book with title, author, publication year, and ISBN.
class BookBase(BaseModel):
    title: str
    author: str
    year: int
    isbn: str


# Schema for creating a new book, inheriting from BookBase.
class BookCreate(BookBase):
    pass


# Schema for updating an existing book, inheriting from BookBase.
class BookUpdate(BookBase):

    # Optional fields allow partial updates.
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[int] = None
    isbn: Optional[str] = None


# Schema for a book retrieved from the database.
class BookInDB(BaseModel):
    id: int
    title: str
    author: str
    year: int
    isbn: str

    @classmethod
    def from_orm(cls, obj):
        # Constructs a BookInDB instance from the ORM object.
        return cls(**obj.__dict__)
