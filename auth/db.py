from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
db_url = 'postgresql://postgres:password@localhost:5432/auth'
engine = create_engine(db_url)
session = sessionmaker(bind=engine, autoflush=False)

SECRET_KEY = 'MY_SECRET_KEY_MR_JHA'
ALGO = 'HS256'
