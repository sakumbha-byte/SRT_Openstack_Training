from sqlalchemy import Column, String, Integer, Float, Date, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
import datetime
import uuid

Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employee'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(256), nullable=False)
    gender = Column(String(8))
    position = Column(String(56))
    salary = Column(Float)
    experience = Column(Integer)
    birth_date = Column(Date)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.datetime.utcnow)
    deleted_at = Column(DateTime)
    deleted = Column(Boolean, default=False)
