from sqlalchemy import Column, Integer, String
from .db import Base


# Create the Book model
class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    isbn = Column(String, nullable=False)
