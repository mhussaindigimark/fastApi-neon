
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class BulkEmailsStatsBase(BaseModel):
    user_id: str
    file_name: str
    user_tested_email: str
    duplicate_email: bool
    total_valid_emails: int
    email_status: str
    is_deliverable: bool
    is_risky: bool
    total: int

class BulkEmailsStatsCreate(BulkEmailsStatsBase):
    pass

class BulkEmailsStats(BulkEmailsStatsBase):
    id: int
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True
