from fastapi import HTTPException
from models.users import User
from sqlalchemy.orm import selectinload, joinedload

def create_user(user, db):
    user_existing = db.query(User).filter_by(email = user.email).first()
    
    if user_existing:
        raise HTTPException(status_code=409, detail='Email already registered!')
    
    new_user = User(name = user.name, email = user.email)
    
    db.add(new_user)
    
    db.commit()
    
    db.refresh(new_user)
    
    return new_user

def get_users(db):
    return db.query(User).all()

def get_users_with_tasks(db):
    return db.query(User).filter(User.tasks.any()).options(selectinload(User.tasks)).all()