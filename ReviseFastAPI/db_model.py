from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
Base = declarative_base()
class Sql_Model(Base):
    __tablename__='prod'
    name=Column(String, primary_key=True)