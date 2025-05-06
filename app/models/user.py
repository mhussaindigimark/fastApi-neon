from sqlalchemy import Column, String, Text, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    user_id = Column(String, primary_key=True)
    email = Column(String(255))
    first_name = Column(String(255))
    last_name = Column(String(255))
    address = Column(Text)
    city = Column(Text)
    gender = Column(Text)
    photo_url = Column(Text)
    country = Column(String(255))
    state = Column(String(255))
    zip_code = Column(String)
    status = Column(Boolean)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
    deleted_by = Column(DateTime)

    # Relationship to UserPermissionRoles
    user_permission_roles = relationship("UserPermissionRoles", back_populates="user")
    # Relationship to BulkEmailsStats
    bulk_emails_stats = relationship("BulkEmailsStats", back_populates="user")
    # Relationship to TestEmail
    test_emails = relationship("TestEmail", back_populates="user")
    # Relationship to Credits
    credits = relationship("Credits", back_populates="user")
    # Relationship to SubscriptionsStripe
    subscriptions_stripes = relationship("SubscriptionsStripe", back_populates="user")
    # Relationship to Invoices
    invoices = relationship("Invoices", back_populates="user")
     # Relationship to CreditHistory
    credit_histories = relationship("CreditHistory", back_populates="user")
    # Relationship to credit_usage
    credit_usages = relationship("CreditUsage", back_populates="user")

