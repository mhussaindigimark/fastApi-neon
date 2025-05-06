
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class InvoicesBase(BaseModel):
    user_id: str
    total: float
    amount: float
    number: str
    tax: float
    card_country: str
    billing_state: str
    billing_zip: str
    billing_country: str

class InvoicesCreate(InvoicesBase):
    pass

class Invoices(InvoicesBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    deleted_by: Optional[datetime] = None

    class Config:
        orm_mode = True
