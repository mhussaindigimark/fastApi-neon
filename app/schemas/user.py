
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class UserBase(BaseModel):
    email: str
    first_name: str
    last_name: str

class UserCreate(UserBase):
    user_id: str
    address: Optional[str] = None
    city: Optional[str] = None
    gender: Optional[str] = None
    photo_url: Optional[str] = None
    country: Optional[str] = None
    state: Optional[str] = None
    zip_code: Optional[str] = None
    status: Optional[bool] = None

class User(UserBase):
    user_id: str
    address: Optional[str] = None
    city: Optional[str] = None
    gender: Optional[str] = None
    photo_url: Optional[str] = None
    country: Optional[str] = None
    state: Optional[str] = None
    zip_code: Optional[str] = None
    status: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    deleted_by: Optional[datetime] = None

    #user_permission_roles: List["UserPermissionRoles"] = []
    #bulk_emails_stats: List["BulkEmailsStats"] = []
    #test_emails: List["TestEmail"] = []
    #credits: List["Credits"] = []
    #subscriptions_stripes: List["SubscriptionsStripe"] = []
    #invoices: List["Invoices"] = []
    class Config:
        orm_mode = True