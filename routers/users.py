from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, selectinload, joinedload
from schemas.users import UserResponse, UserCreate, UserUpdate, UserWithTasksResponse
from database import get_db
from models.users import User
from typing import List
from services import users

router = APIRouter()

@router.post('/users', status_code=201, response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return users.create_user(user, db)
    
@router.get('/users', status_code=200, response_model=List[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return users.get_users(db)
    
@router.get('/users/users-with-tasks', status_code=200, response_model=List[UserWithTasksResponse])
def get_users_with_tasks(db: Session = Depends(get_db)):
    return users.get_users_with_tasks(db)

@router.get('/users/{user_id}/tasks', response_model=UserWithTasksResponse)
def get_user_tasks(user_id: int, db: Session = Depends(get_db)):
    user_tasks = db.query(User).filter_by(id = user_id).options(joinedload(User.tasks)).first()
    
    if not user_tasks:
        raise HTTPException(status_code=404, detail='Id not exists!')
    
    return user_tasks

@router.get('/users/{id_user}', status_code=200, response_model=UserResponse)
def get_user(id_user: int, db: Session = Depends(get_db)):
    user_exists = db.query(User).filter_by(id = id_user).first()
    
    if not user_exists:
        raise HTTPException(status_code=404, detail='Id not exists!')
    
    return user_exists

@router.delete('/users/{id_user}', status_code=204)
def delete_user(id_user: int, db: Session = Depends(get_db)):
    user_exists = db.query(User).filter_by(id = id_user).first()
    
    if not user_exists:
        raise HTTPException(status_code=404, detail='Id not exists!')
    
    db.query(User).filter_by(id = id_user).delete()
    
    db.commit()
    
@router.put('/users/{id_user}', status_code=200, response_model=UserResponse)
def update_user(id_user: int, user_updated: UserUpdate, db: Session = Depends(get_db)):
    get_user = db.query(User).filter_by(id = id_user).first()
    
    if not get_user:
        raise HTTPException(status_code=404, detail='Id not exists!')
    
    email_existing = db.query(User).filter_by(email = user_updated.email).first()
    
    if email_existing and email_existing.id != id_user:
        raise HTTPException(status_code=409, detail='Email already registered!')
    
    get_user.name = user_updated.name
    get_user.email = user_updated.email
    
    db.commit()
    
    db.refresh(get_user)
    
    return get_user