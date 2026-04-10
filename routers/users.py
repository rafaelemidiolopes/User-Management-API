from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.users import UserResponse, UserCreate, UserUpdate, UserWithTasksResponse, UserLogin, Token
from database import get_db
from services import users
from services.security import get_current_user
from models.users import User
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

@router.post('/users', status_code=201, response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return users.create_user(user, db)
    
@router.post('/login', response_model=Token) 
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)): 
    return users.login(form_data, db) 
    
@router.get('/me', response_model = UserResponse)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user    
    
@router.get('/users', response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return users.get_users(db)
    
@router.get('/users/users-with-tasks', response_model=list[UserWithTasksResponse])
def get_users_with_tasks(db: Session = Depends(get_db)):
    return users.get_users_with_tasks(db)

@router.get('/users/{user_id}/tasks', response_model=UserWithTasksResponse)
def get_user_tasks(user_id: int, db: Session = Depends(get_db)):
    return users.get_user_tasks(user_id, db)

@router.get('/users/{user_id}', response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return users.get_user_or_404(user_id, db)

@router.delete('/users/{user_id}', status_code=204)
def delete_user(user_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    users.delete_user(user_id, current_user, db)
    
@router.put('/users/{user_id}', response_model=UserResponse)
def update_user(user_id: int, user_updated: UserUpdate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return users.update_user(user_id, user_updated, db)