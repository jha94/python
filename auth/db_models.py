from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String

Base = declarative_base()

class Prod(Base):
    __tablename__ = 'user'
    email=Column(String, primary_key=True)
    password=Column(String)
