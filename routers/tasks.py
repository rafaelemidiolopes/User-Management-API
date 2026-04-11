from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.tasks import TaskResponse, TaskUpdate, TaskCreate
from database import get_db
from services import tasks
from services.security import get_current_admin
from models.users import User

router = APIRouter()

@router.post('/tasks', status_code=201, response_model=TaskResponse)
def create_task(task: TaskCreate, current_admin: User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return tasks.create_task(task, db)

@router.get('/tasks', response_model=list[TaskResponse])
def get_tasks(current_admin: User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return tasks.get_tasks(db)

@router.get('/tasks/{task_id}', response_model=TaskResponse)
def get_task(task_id: int, current_admin: User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return tasks.get_task_or_404(task_id, db)

@router.put('/tasks/{task_id}', response_model=TaskResponse)
def update_task(task_id: int, task_updated: TaskUpdate, current_admin: User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return tasks.update_task(task_id, task_updated, db)

@router.delete('/tasks/{task_id}', status_code=204)
def delete_task(task_id: int, current_admin: User = Depends(get_current_admin), db: Session = Depends(get_db)):
    tasks.delete_task(task_id, db)