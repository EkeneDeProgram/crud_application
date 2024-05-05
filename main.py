from fastapi import FastAPI
from app.db import engine
from app.routes import router
from app.models import Base

app = FastAPI()  # Initialize FastAPI.

# Specify prefix in the app.
app.include_router(router, prefix="/api")

# Create the database tables
Base.metadata.create_all(bind=engine)