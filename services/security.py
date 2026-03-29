from pwdlib import PasswordHash
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from jwt import encode

hasher = PasswordHash.recommended()

SECRET_KEY = '12345'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def get_password_hash(password: str):
    return hasher.hash(password)

def verify_password(password: str, hash_password: str):
    return hasher.verify(password, hash_password)

def create_token(data: dict):
    to_encode = data.copy()
    
    expire = datetime.now(tz= ZoneInfo('UTC')) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp': expire})
    
    encoded_jwt = encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)
    
    return encoded_jwt