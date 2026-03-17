from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from typing import List
from schemas.tasks import TaskResponse, TaskUpdate
from database import get_db
from models.tasks import Task

router = APIRouter()

@router.get('/tasks', response_model=List[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    return db.query(Task).options(joinedload(Task.user)).all()

@router.get('/tasks/{task_id}', response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    return db.query(Task).filter_by(id = task_id).all()

@router.put('/tasks/{task_id}', response_model=TaskResponse)
def update_task(task_id: int, task_updated = TaskUpdate, db: Session = Depends(get_db)):
    task = db.query(Task).filter_by(id = task_id).all()
    
    if not task:
        raise HTTPException(status_code=404, detail='Task not found! ')
    
    task.name = task_updated.name
    task.description = task_updated.description
    
    db.commit()
    db.refresh(Task)
    
    return task

@router.delete('/tasks/{task_id}', status_code=204)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter_by(id = task_id).first()
    
    if not task:
        raise HTTPException(status_code=404, detail='Task not found! ')
        
    db.delete(task)
    db.commit()
    
@router.get('/tasks/tasks-with-user', response_model=List[TaskResponse])
def get_tasks_with_user(db: Session = Depends(get_db)):
    return db.query(Task).options(joinedload(Task.user)).all()