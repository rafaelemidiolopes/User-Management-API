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
    return users.get_user_tasks(user_id, db)

@router.get('/users/{id_user}', status_code=200, response_model=UserResponse)
def get_user(id_user: int, db: Session = Depends(get_db)):
    return users.get_user_or_404(id_user, db)

@router.delete('/users/{id_user}', status_code=204)
def delete_user(id_user: int, db: Session = Depends(get_db)):
    users.delete_user(id_user, db)
    
@router.put('/users/{id_user}', status_code=200, response_model=UserResponse)
def update_user(id_user: int, user_updated: UserUpdate, db: Session = Depends(get_db)):
    return users.delete_user(id_user, user_updated, db)