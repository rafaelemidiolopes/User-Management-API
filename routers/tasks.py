from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from typing import List
from schemas.tasks import TaskResponse, TaskUpdate, TaskCreate
from database import get_db
from models.tasks import Task
from models.users import User

router = APIRouter()

@router.post('/tasks', status_code=201, response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    new_task = Task(title = task.title, description = task.description, user_id = task.user_id)
    
    if new_task.user_id != None:
        user_exists = db.query(User).filter_by(id = task.user_id).first()
    
        if not user_exists:
            raise HTTPException(status_code=404, detail='User id not found! ')
    
    db.add(new_task)
    
    db.commit()
    
    db.refresh(new_task)
    
    return new_task

@router.get('/tasks', response_model=List[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    return db.query(Task).options(joinedload(Task.user)).all()
    
@router.get('/tasks/tasks-with-user', response_model=List[TaskResponse])
def get_tasks_with_user(db: Session = Depends(get_db)):
    return db.query(Task).filter(Task.user_id != None).options(joinedload(Task.user)).all()

@router.get('/tasks/tasks-without-user', response_model=List[TaskResponse])
def get_tasks_without_user(db: Session = Depends(get_db)):
    return db.query(Task).filter(Task.user_id.is_(None)).all()

@router.get('/tasks/{task_id}', response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    return db.query(Task).filter_by(id = task_id).first()

@router.put('/tasks/{task_id}', response_model=TaskResponse)
def update_task(task_id: int, task_updated = TaskUpdate, db: Session = Depends(get_db)):
    task = db.query(Task).filter_by(id = task_id).first()
    
    if not task:
        raise HTTPException(status_code=404, detail='Task not found! ')
    
    task.name = task_updated.name
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