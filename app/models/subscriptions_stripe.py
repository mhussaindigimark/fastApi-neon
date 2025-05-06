
from sqlalchemy import Column, String, BigInteger, Boolean, DateTime, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class SubscriptionsStripe(Base):
    __tablename__ = "subscriptions_stripe"

    subscription_id = Column(BigInteger, primary_key=True)
    user_id = Column(String, ForeignKey("user.user_id"))
    plan_id = Column(Integer, ForeignKey("pricing_plans.plan_id"), nullable=False)
    stripe_subscription_id = Column(String)
    stripe_customer_id = Column(String)
    subscription_plan = Column(String)
    status = Column(Boolean)
    current_period_start = Column(DateTime)
    current_period_end = Column(DateTime)
    cancel_at = Column(DateTime)
    created_at = Column(DateTime)
    ended_at = Column(DateTime)

    # Relationship to User
    user = relationship("User", back_populates="subscriptions_stripes")
    # Relationship to PricingPlans
    pricing_plan = relationship("PricingPlans", back_populates="subscriptions_stripes")

