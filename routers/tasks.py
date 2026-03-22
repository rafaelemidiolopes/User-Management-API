from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from typing import List
from schemas.tasks import TaskResponse, TaskUpdate, TaskCreate
from database import get_db
from models.tasks import Task
from models.users import User
from services import users, tasks

router = APIRouter()

@router.post('/tasks', status_code=201, response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return tasks.create_task(task, db)

@router.get('/tasks', response_model=List[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    return tasks.get_tasks(db)
    
@router.get('/tasks/tasks-with-user', response_model=List[TaskResponse])
def get_tasks_with_user(db: Session = Depends(get_db)):
    return tasks.get_tasks_with_user(db)

@router.get('/tasks/tasks-without-user', response_model=List[TaskResponse])
def get_tasks_without_user(db: Session = Depends(get_db)):
    return tasks.get_tasks_without_user(db)

@router.get('/tasks/{task_id}', response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    return tasks.get_task(db, task_id)

@router.put('/tasks/{task_id}', response_model=TaskResponse)
def update_task(task_id: int, task_updated: TaskUpdate, db: Session = Depends(get_db)):
    task = db.query(Task).filter_by(id = task_id).first()
    
    if not task:
        raise HTTPException(status_code=404, detail='Task not found! ')
    
    if task_updated.user_id == 0:
        task_updated.user_id = None
    
    if task_updated.user_id != None:
        user = db.query(User).filter_by(id = task_updated.user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail='User not found! ')

    task.title = task_updated.title
    task.description = task_updated.description
    task.status = task_updated.status
    task.user_id = task_updated.user_id
        
    db.commit()
    db.refresh(task)
    
    return task

@router.delete('/tasks/{task_id}', status_code=204)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter_by(id = task_id).first()
    
    if not task:
        raise HTTPException(status_code=404, detail='Task not found! ')
        
    db.delete(task)
    db.commit()