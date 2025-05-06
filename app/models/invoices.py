
from sqlalchemy import Column, String, BigInteger, Numeric, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Invoices(Base):
    __tablename__ = "invoices"

    id = Column(BigInteger, primary_key=True)
    user_id = Column(String, ForeignKey("user.user_id"))
    total = Column(Numeric(8, 2))
    amount = Column(Numeric)
    number = Column(String)
    tax = Column(Numeric(8, 2))
    card_country = Column(String(255))
    billing_state = Column(String(255))
    billing_zip = Column(String(255))
    billing_country = Column(String(255))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
    deleted_by = Column(DateTime)

    # Relationship to User
    user = relationship("User", back_populates="invoices")

