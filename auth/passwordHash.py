from pwdlib import PasswordHash
import jwt
from db import SECRET_KEY, ALGO

password_hash = PasswordHash.recommended()

def get_password_hash(password:str) -> str:
    return password_hash.hash(password)

def createAccessToken(data:dict) -> str:
    return jwt.encode(data, SECRET_KEY, algorithm=ALGO or "HS256")

def decodeAccessToken(token:str) -> str:
    return jwt.decode(token, SECRET_KEY, algorithm=ALGO or "HS256")