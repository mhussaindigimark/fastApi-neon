from fastapi import FastAPI
from app.routes.base import router as base_router
from app.database.connection import Base, engine



import os
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from typing import List
from datetime import datetime
from pydantic import BaseModel
from sqlalchemy import Column, String, Text, Boolean, DateTime, Integer, ForeignKey, Numeric, BigInteger, Float, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from fastapi import Depends, HTTPException
from typing import Optional


# load_dotenv()

# # Database Configuration
# DB_USER = os.environ.get("DB_USER")
# DB_PASS = os.environ.get("DB_PASS")
# DB_HOST = os.environ.get("DB_HOST")
# DB_PORT = os.environ.get("DB_PORT")
# DB_NAME = os.environ.get("DB_NAME")

# SQLALCHEMY_DATABASE_URL = (
#      f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
#  )

# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def create_app():
    app = FastAPI(
        title="FastAPI Neon Boilerplate",
        description="Boilerplate for FastAPI with Neon DB",
        version="0.1.0"
    )
    
    # Create database tables
    Base.metadata.create_all(bind=engine)
    
    # Include routers
    app.include_router(base_router, prefix="/api/v1")
    
    return app

app = create_app()