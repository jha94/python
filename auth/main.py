from fastapi import FastAPI, Depends
from db_model import Base, DB_User
from db import engine, session
from local_model import Local_User
from sqlalchemy.orm import Session
from utils import get_hash_password, encode_token, token_validity

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
def sign_up(user:Local_User,db:Session = Depends(get_db)):
    db.add(DB_User(
        email=user.email,
        password=get_hash_password(user.password)
    ))
    db.commit()
    token = encode_token({
        'email':user.email
    })
    return {
        'message':'Signed up successfully',
        'auth_token':token
    }

@app.post('/secure')
def secure(user:DB_User=Depends(token_validity)):
    return {
        'message':'token is valid',
        'email':user.email
    }