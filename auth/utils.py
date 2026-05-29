from pwdlib import PasswordHash
import jwt
from db import SECRET_KEY, ALGO
from datetime import datetime, timedelta, timezone

password_hash = PasswordHash.recommended()

def hash_password(password:str) -> str:
    return password_hash.hash(password)

def encode_access_token(data:dict, expires_at:timedelta=None) -> str:
    if expires_at:
        expire = datetime.now(timezone.utc)+expires_at
    else:
        expire = datetime.now(timezone.utc)+timedelta(minutes=60)
    data.update({'exp':expire})
    return jwt.encode(data, SECRET_KEY, algorithm=ALGO or 'HS256')