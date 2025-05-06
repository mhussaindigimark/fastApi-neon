
from sqlalchemy import Column, String, BigInteger, Integer, Numeric, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class CreditUsage(Base):
    __tablename__ = "credit_usage"

    usage_id = Column(BigInteger, primary_key=True)
    user_id = Column(String, ForeignKey("user.user_id"))
    email_or_file_id = Column(BigInteger)  # e.g., file ID or single email ID
    quantity_used = Column(Integer)  # e.g., how many emails were validated
    credits_used = Column(Numeric(8, 2))
    created_at = Column(DateTime)

     # Relationship to User
    user = relationship("User", back_populates="credit_usages")
    
    
    