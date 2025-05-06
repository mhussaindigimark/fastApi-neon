from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.user import UserBase

router = APIRouter()

# @router.get("/", response_model=UserBase)
# def root(db: Session = Depends(get_db)):
#     return {"message": "Welcome to FastAPI with Neon DB"}

@router.get("/")
def read_root():
    return {"Hello": "World"}