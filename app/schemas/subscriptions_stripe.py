
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SubscriptionsStripeBase(BaseModel):
    user_id: str
    plan_id: int
    stripe_subscription_id: str
    stripe_customer_id: str
    subscription_plan: str
    status: bool
    current_period_start: datetime
    current_period_end: datetime
    cancel_at: Optional[datetime] = None

class SubscriptionsStripeCreate(SubscriptionsStripeBase):
    pass

class SubscriptionsStripe(SubscriptionsStripeBase):
    subscription_id: int
    created_at: Optional[datetime] = None
    ended_at: Optional[datetime] = None

    class Config:
        orm_mode = True