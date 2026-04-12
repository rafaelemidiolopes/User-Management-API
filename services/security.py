from pwdlib import PasswordHash
from datetime import datetime, timedelta
from http import HTTPStatus
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from zoneinfo import ZoneInfo
from jwt import encode, decode, DecodeError, ExpiredSignatureError
from sqlalchemy import select
from database import get_db
from sqlalchemy.orm import Session
from models.users import User
from dotenv import load_dotenv
import os

hasher = PasswordHash.recommended()

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
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

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


def get_current_user(
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme),
):
    credentials_exception = HTTPException(
        status_code=HTTPStatus.UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'})

    try:
        payload = decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get('sub')
        user_id = int(user_id)

        if not user_id:
            raise credentials_exception
        
    except ExpiredSignatureError:
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED,
            detail='Token expired',
            headers={'WWW-Authenticate': 'Bearer'})

    except DecodeError:
        raise credentials_exception

    except Exception:
        raise credentials_exception
        
    user = db.scalar(
        select(User).where(User.id == user_id)
    )

    if not user:
        raise credentials_exception

    return user

def get_current_admin(current_user: User = Depends(get_current_user)):
    
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail='Unauthorized')
    
    return current_user