from pwdlib import PasswordHash
import jwt
from db import SECRET_KEY, ALGO
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from db_models import db_user
from sqlalchemy.orm import Session
from db import session

passwordHash = PasswordHash.recommended()

oauth_scheme = OAuth2PasswordBearer(tokenUrl='login')

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

def get_hashed_password(password:str) -> str:
   return passwordHash.hash(password)

def encode_password(user_data:dict, expires_at:timedelta=None) -> str:
   if(expires_at):
      expires = datetime.now(timezone.utc)+expires_at
   else:
      expires = datetime.now(timezone.utc)+timedelta(minutes=60)
   user_data.update({
      'exp':expires
   })
   return jwt.encode(user_data, SECRET_KEY, algorithm=ALGO or 'HS256')


def get_current_user(token: str = Depends(oauth_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGO or 'HS256'])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except jwt.PyJWTError:
        raise credentials_exception
    user = db.query(db_user).filter(db_user.email == email).first()
    if user is None:
        raise credentials_exception
    return user 

