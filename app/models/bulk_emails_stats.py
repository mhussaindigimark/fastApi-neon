
from sqlalchemy import Column, String, BigInteger, Boolean, Integer, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class BulkEmailsStats(Base):
    __tablename__ = "bulk_emails_stats"

    id = Column(BigInteger, primary_key=True)
    user_id = Column(String, ForeignKey("user.user_id"))
    file_name = Column(String(255))
    user_tested_email = Column(Text)
    duplicate_email = Column(Boolean)
    total_valid_emails = Column(Integer)
    email_status = Column(Text)
    is_deliverable = Column(Boolean)
    is_risky = Column(Boolean)
    total = Column(Integer)
    created_at = Column(DateTime)

    # Relationship to User
    user = relationship("User", back_populates="bulk_emails_stats")

