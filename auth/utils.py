from pwdlib import PasswordHash
import jwt
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from db import session
from sqlalchemy.orm import Session
from db_model import DB_User

ALGO = 'HS256'
SECRET_KEY = 'MY_SECRET_KEY_256_MY_SECRET_KEY'

hash_password = PasswordHash.recommended()

OAuth_scheme = OAuth2PasswordBearer(tokenUrl='sign_up')

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


def get_hash_password(password:str) ->str:
    return hash_password.hash(password)

def encode_token(user_data:dict, expires_at:timedelta=None) ->str:
    expires_at = datetime.now(timezone.utc) + (expires_at or timedelta(minutes=60))
    user_data.update({
        'exp':expires_at
    })
    return jwt.encode(user_data, SECRET_KEY, algorithm=ALGO)

def token_validity(token:str = Depends(OAuth_scheme), db:Session=Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Invalid Token',
        headers={'WWW-Authenticate': 'Bearer'}
    )
    try:
        paylaod = jwt.decode(token, SECRET_KEY, algorithms=[ALGO or 'HS256'])
        email = paylaod.get('email')
        if email is None:
            raise credentials_exception
    except jwt.PyJWTError:
        raise credentials_exception
    user = db.query(DB_User).filter(DB_User.email==email).first()
    if user is None:
        raise credentials_exception
    return user
