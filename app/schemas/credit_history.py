
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CreditHistoryBase(BaseModel):
    user_id: str
    credits_purchased: float
    amount: float
    purchased_at: datetime

class CreditHistoryCreate(CreditHistoryBase):
    pass

class CreditHistory(CreditHistoryBase):
    purchase_id: int

    class Config:
        orm_mode = True
