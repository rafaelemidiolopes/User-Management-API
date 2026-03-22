from models.tasks import Task
from models.users import User
from fastapi import HTTPException
from sqlalchemy.orm import joinedload

def create_task(task, db):    
    new_task = Task(title = task.title, description = task.description, user_id = task.user_id)
    
    if new_task.user_id == 0:
        new_task.user_id = None
    
    if new_task.user_id != None:
        user_exists = db.query(User).filter_by(id = task.user_id).first()
    
        if not user_exists:
            raise HTTPException(status_code=404, detail='User id not found! ')
    
    db.add(new_task)
    
    db.commit()
    
    db.refresh(new_task)
    
    return new_task

def get_tasks(db):
    return db.query(Task).options(joinedload(Task.user)).all()

def get_tasks_with_user(db):
    return db.query(Task).filter(Task.user_id != None).options(joinedload(Task.user)).all()

def get_tasks_without_user(db):
    return db.query(Task).filter(Task.user_id.is_(None)).all()