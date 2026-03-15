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