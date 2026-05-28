from fastapi import FastAPI, Depends
import db_models
from db import engine, session
from models import user_type
from sqlalchemy.orm import Session
from passwordHash import get_password_hash, createAccessToken

app = FastAPI()
db_models.Base.metadata.create_all(bind=engine)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
def start():
    return 'server started'

@app.post('/add_user')
def add_user(user:user_type, db:Session=Depends(get_db)):
    user_data = db_models.Prod(
        email=user.email,
        password=get_password_hash(user.password)
    )
    db.add(user_data)
    db.commit()
    return {"message": "user added",'email':user.email, 'password':get_password_hash(user.password)}

@app.post('/login')
def login(user:user_type, db:Session=Depends(get_db)):
    user = db.query(db_models.Prod).filter(db_models.Prod.email==user.email).first()
    if not user:
        return {"error": "user not found"}
    token_payload = {"email": user.email, "password":user.password}
    token = createAccessToken(token_payload)
    return {
        "message": "Login Successful",
        "data": {
            "email": user.email,
            "access_token": "Bearer "+ token 
        }
    }


