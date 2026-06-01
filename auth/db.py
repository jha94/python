from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = 'postgresql://postgres:password@localhost:5432/auth'
engine = create_engine(db_url)

session = sessionmaker(bind=engine, autoflush=False)

SECRET_KEY = 'MY_SECRET_KEY'
ALGO = 'HS256'