from fastapi import FastAPI, Depends
from db_models import Base, db_user
from db import engine, session
from models import User
from sqlalchemy.orm import Session
from utils import get_hashed_password, encode_password, get_current_user

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
def sign_up(user:User, db:Session = Depends(get_db)):
    hashedUser =db_user(
        email=user.email,
        password=get_hashed_password(user.password)
    )
    db.add(hashedUser)
    db.commit()
    token_data = {"sub": user.email} 
    token = encode_password(token_data)
    
    return {
        "access_token": token, 
        "token_type": "bearer"
    }

@app.post('/protected-route')
def secure_data(current_user: db_user = Depends(get_current_user)):
    return {"message": f"Hello {current_user.email}, your account is active!"}