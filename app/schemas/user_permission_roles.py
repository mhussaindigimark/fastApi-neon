
from pydantic import BaseModel
from datetime import datetime

class UserPermissionRolesBase(BaseModel):
    user_id: str
    role_id: int

class UserPermissionRolesCreate(UserPermissionRolesBase):
    pass

class UserPermissionRoles(UserPermissionRolesBase):
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True
