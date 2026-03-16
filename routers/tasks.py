from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, joinedload
from typing import List
from schemas.tasks import TaskResponse
from database import get_db
from models.tasks import Task

router = APIRouter()

@router.get('/tasks', response_model=List[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    return db.query(Task).options(joinedload(Task.user)).all()

@router.get('/tasks/{task_id}', response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    return db.query(Task).filter_by(id = task_id).all()