from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = "postgresql://postgres:password@localhost:5432/first"
engine = create_engine(db_url)
session = sessionmaker(autoflush=False, autocommit=False, bind=engine)