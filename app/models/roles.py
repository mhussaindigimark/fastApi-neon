
from sqlalchemy import Column, String, Integer, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Roles(Base):
    __tablename__ = "roles"

    role_id = Column(Integer, primary_key=True, autoincrement=True)
    role_name = Column(String(255), unique=True)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

    # Relationship to UserPermissionRoles
    user_permission_roles = relationship("UserPermissionRoles", back_populates="role")
