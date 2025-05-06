
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PricingPlansBase(BaseModel):
    plan_name: str

class PricingPlansCreate(PricingPlansBase):
    pass

class PricingPlans(PricingPlansBase):
    plan_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True