
from sqlalchemy import Column, Integer, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserPermissionRoles(Base):
    __tablename__ = "user_permission_roles"

    user_id = Column(Integer, ForeignKey("user.user_id"), primary_key=True)
    role_id = Column(Integer, ForeignKey("roles.role_id"), primary_key=True)
    created_at = Column(TIMESTAMP)

    # Relationship to User
    user = relationship("User", back_populates="user_permission_roles")
    # Relationship to Roles
    role = relationship("Roles", back_populates="user_permission_roles")