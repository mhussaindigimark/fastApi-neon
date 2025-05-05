from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.base import BaseSchema

router = APIRouter()

@router.get("/", response_model=BaseSchema)
def root(db: Session = Depends(get_db)):
    return {"message": "Welcome to FastAPI with Neon DB"}