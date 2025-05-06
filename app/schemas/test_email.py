
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TestEmailBase(BaseModel):
    user_id: str
    user_tested_email: str
    full_name: str
    gender: str
    status: str
    reason: str
    domain: str
    is_free: bool
    is_valid: bool
    is_disposable: bool
    has_tag: bool
    alphabetical_characters: int
    is_mailbox_full: bool
    has_role: bool
    is_accept_all: bool
    has_numerical_characters: int
    has_unicode_symbols: int
    has_no_reply: bool
    smtp_provider: str
    mx_record: str
    implicit_mx_record: str
    score: int

class TestEmailCreate(TestEmailBase):
    pass

class TestEmail(TestEmailBase):
    id: int
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True

