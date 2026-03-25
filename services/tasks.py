from models.tasks import Task
from models.users import User
from fastapi import HTTPException
from sqlalchemy.orm import joinedload

def create_task(task, db):    
    new_task = Task(title = task.title, description = task.description, status = task.status, user_id = task.user_id)

    if new_task.user_id is not None:
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
    return db.query(Task).filter(Task.user_id.isnot(None)).options(joinedload(Task.user)).all()

def get_tasks_without_user(db):
    return db.query(Task).filter(Task.user_id.is_(None)).all()

def get_task(db, task_id):
    return get_task_or_404(db, task_id)

def update_task(task_id, task_updated, db):
    task = get_task_or_404(db, task_id)
    
    if task_updated.user_id is not None:
        user = db.query(User).filter_by(id = task_updated.user_id).first()
        
        if not user:
            raise HTTPException(status_code=404, detail='User not found! ')

    dict_task_updated = task_updated.model_dump(exclude_unset = True)
    
    for field, value in dict_task_updated.items():
        setattr(task, field, value)
        
    db.commit()
    
    db.refresh(task)
    
    return task

def delete_task(task_id, db):
    task = get_task_or_404(db, task_id)
        
    db.delete(task)
    db.commit()
    
def get_task_or_404(db, task_id):
    task = db.query(Task).filter_by(id = task_id).first()
    
    if not task:
        raise HTTPException(status_code=404, detail='Task not found! ')
    
    return task