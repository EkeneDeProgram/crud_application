from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Load environmental variables from .env file
load_dotenv()

# Access environmental variables
DATABASE_URL = os.getenv("DATABASE_URL")

# Initialize SQLAlchemy engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declare the base class for SQLAlchemy models.
Base = declarative_base()


# Function to obtain a database session.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
