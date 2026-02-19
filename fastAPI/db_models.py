from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = 'First'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    desc = Column(String, index=True)