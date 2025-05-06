
from sqlalchemy import Column, String, BigInteger, Boolean, Integer, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class TestEmail(Base):
    __tablename__ = "test_email"

    id = Column(BigInteger, primary_key=True)
    user_id = Column(String, ForeignKey("user.user_id"))
    user_tested_email = Column(Text)
    full_name = Column(String(255))
    gender = Column(Text)
    status = Column(Text)
    reason = Column(Text)
    domain = Column(String(255))
    is_free = Column(Boolean)
    is_valid = Column(Boolean)
    is_disposable = Column(Boolean)
    has_tag = Column(Boolean)
    alphabetical_characters = Column(Integer)
    is_mailbox_full = Column(Boolean)
    has_role = Column(Boolean)
    is_accept_all = Column(Boolean)
    has_numerical_characters = Column(Integer)
    has_unicode_symbols = Column(Integer)
    has_no_reply = Column(Boolean)
    smtp_provider = Column(String(255))
    mx_record = Column(String(255))
    implicit_mx_record = Column(String(255))
    score = Column(Integer)
    created_at = Column(DateTime)

    # Relationship to User
    user = relationship("User", back_populates="test_emails")

