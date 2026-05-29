from fastapi import FastAPI, Depends
from db_models import Base, DB_USER
from db import engine, session
from models import User
from sqlalchemy.orm import Session
from utils import hash_password, encode_access_token

app = FastAPI()
Base.metadata.create_all(bind=engine)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
def start():
    return 'Server started'

@app.post('/sign_up')
def sign_up(user:User, db:Session=Depends(get_db)):
    user = DB_USER(
        email=user.email,
        password= hash_password(user.password)
    )
    db.add(user)
    db.commit()
    return 'user added'

@app.post('/log_in')
def log_in(user:User, db:Session=Depends(get_db)):
    found_user = db.query(DB_USER).filter(DB_USER.email==user.email).first()
    if not found_user:
        return 'User is not registered'
    user_data = encode_access_token({
        'email':user.email,
        'password':user.password
    })
    return user_data
