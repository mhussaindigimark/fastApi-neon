from sqlalchemy import Column, Integer
from app.database.connection import Base

class BaseModel(Base):
    __abstract__ = True
    
    id = Column(Integer, primary_key=True, index=True)
    
    def __repr__(self):
        return f"<{type(self).__name__}(id={self.id})>"