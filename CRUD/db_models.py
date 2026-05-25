from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String
Base = declarative_base()

class Prod(Base):
    __tablename__ = 'Prod'
    id=Column(Integer, primary_key=True)
    name=Column(String)
    desc=Column(String)
    float=Column(Float)