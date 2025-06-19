# models/activity_model.py

from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from models.category_model import Base
from datetime import datetime

class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(Text, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    response_time_seconds = Column(Float, nullable=True)

    category = relationship("Category")
