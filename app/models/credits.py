
from sqlalchemy import Column, String, BigInteger, Boolean, Numeric, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Credits(Base):
    __tablename__ = "credits"

    credit_id = Column(BigInteger, primary_key=True)
    user_id = Column(String, ForeignKey("user.user_id"))
    credits = Column(Numeric(8, 2))
    is_paid = Column(Boolean)
    total_credits = Column(Integer)
    remaining_credits = Column(Integer)
    last_updated = Column(DateTime)
    created_at = Column(DateTime)
    expires_at = Column(DateTime)

    # Relationship to User
    user = relationship("User", back_populates="credits")

