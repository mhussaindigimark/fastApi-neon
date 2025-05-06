
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class RolesBase(BaseModel):
    role_name: str

class RolesCreate(RolesBase):
    pass

class Roles(RolesBase):
    role_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    #user_permission_roles: List["UserPermissionRoles"] = []

    class Config:
        orm_mode = True
