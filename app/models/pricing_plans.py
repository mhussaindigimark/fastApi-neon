
from sqlalchemy import Column, String, Integer, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PricingPlans(Base):
    __tablename__ = "pricing_plans"

    plan_id = Column(Integer, primary_key=True, autoincrement=True)
    plan_name = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
    #Relationship to subscriptions
    subscriptions_stripes = relationship("SubscriptionsStripe", back_populates="pricing_plan")

