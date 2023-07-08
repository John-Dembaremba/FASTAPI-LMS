from sqlalchemy.orm import declarative_mixin
from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func

@declarative_mixin
class TimeStamp:
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, nullable=False, onupdate=func.now())