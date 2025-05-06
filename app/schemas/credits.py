
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CreditsBase(BaseModel):
    user_id: str
    credits: float
    is_paid: bool
    total_credits: int
    remaining_credits: int

class CreditsCreate(CreditsBase):
    pass

class Credits(CreditsBase):
    credit_id: int
    last_updated: Optional[datetime] = None
    created_at: Optional[datetime] = None
    expires_at: Optional[datetime] = None

    class Config:
        orm_mode = True

