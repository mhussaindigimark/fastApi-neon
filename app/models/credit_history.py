
from sqlalchemy import Column, String, BigInteger, Numeric, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class CreditHistory(Base):
    __tablename__ = "credit_history"

    purchase_id = Column(BigInteger, primary_key=True)
    user_id = Column(String, ForeignKey("user.user_id"))
    credits_purchased = Column(Numeric(8, 2))
    amount = Column(Float)
    purchased_at = Column(DateTime)

    # Relationship to User
    user = relationship("User", back_populates="credit_histories")

