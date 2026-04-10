from fastapi import HTTPException
from models.users import User
from sqlalchemy.orm import selectinload, joinedload, Session
from schemas.users import UserCreate, UserUpdate, UserLogin, Token
from sqlalchemy import select
from services.security import verify_password, get_password_hash, create_token
from fastapi.security import OAuth2PasswordRequestForm

def create_user(user: UserCreate, db: Session) -> User:
    email_existing = db.scalar(select(User).where(User.email == user.email))
    
    if email_existing:
        raise HTTPException(status_code=409, detail='Email already registered!')
    
    password_hash = get_password_hash(user.password)
    
    new_user = User(name = user.name, email = user.email, password_hash = password_hash)
    
    db.add(new_user)
    
    db.commit()
    
    db.refresh(new_user)
    
    return new_user

def get_users(db: Session) -> list[User]:
    return db.query(User).all()

def get_users_with_tasks(db: Session) -> list[User]:
    return db.query(User).filter(User.tasks.any()).options(selectinload(User.tasks)).all()

def get_user_tasks(user_id: int, db: Session) -> User:
    user_with_tasks = db.query(User).filter_by(id = user_id).options(joinedload(User.tasks)).first()
    
    if not user_with_tasks:
        raise HTTPException(status_code=404, detail='User not found!')
    
    return user_with_tasks

def delete_user(user_id: int, current_user: User, db: Session) -> None:
    if user_id != current_user.id:
        raise HTTPException(status_code=403)
    
    user = get_user_or_404(user_id, db)
    
    db.delete(user)
    
    db.commit()
    
def update_me(current_user: User, user_updated: UserUpdate, db: Session) -> User:
    if user_updated.email:
        user = db.query(User).filter_by(email = user_updated.email).first()
    
        if user and user.id != current_user.id:
            raise HTTPException(status_code=409, detail='Email already registered!')
    
    dict_user_updated = user_updated.model_dump(exclude_unset = True)
    
    for field, value in dict_user_updated.items():
        setattr(current_user, field, value)
    
    db.commit()
    
    db.refresh(current_user)
    
    return current_user

def get_user_or_404(user_id: int, db: Session) -> User:
    user = db.query(User).filter_by(id = user_id).first()
    
    if not user:
        raise HTTPException(status_code=404, detail='User not found!')
    
    return user

def login(form_data: OAuth2PasswordRequestForm, db: Session) -> Token: 
    user = db.query(User).filter_by(email = form_data.username).first() 
    
    if not user: 
        raise HTTPException(status_code = 401, detail = 'Invalid credentials! ') 
    
    if not verify_password(form_data.password, user.password_hash): 
        raise HTTPException(status_code = 401, detail = 'Invalid credentials! ') 
    
    token = create_token({'sub': str(user.id)}) 
    
    return Token(access_token=token, token_type='bearer')