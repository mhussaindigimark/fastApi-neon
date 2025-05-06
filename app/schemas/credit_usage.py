
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CreditUsageBase(BaseModel):
    user_id: str
    email_or_file_id: int
    quantity_used: int
    credits_used: float
    created_at: datetime

class CreditUsageCreate(CreditUsageBase):
    pass

class CreditUsage(CreditUsageBase):
    usage_id: int

    class Config:
        orm_mode = True
