from fastapi import HTTPException
from models.users import User
from sqlalchemy.orm import selectinload, joinedload

def create_user(user, db):
    email_existing = db.query(User).filter_by(email = user.email).first()
    
    if email_existing:
        raise HTTPException(status_code=409, detail='Email already registered!')
    
    new_user = User(name = user.name, email = user.email)
    
    db.add(new_user)
    
    db.commit()
    
    db.refresh(new_user)
    
    return new_user

def get_users(db):
    return db.query(User).all()

def get_users_with_tasks(db):
    return db.query(User).filter(User.tasks.any()).options(selectinload(User.tasks)).all()

def get_user_tasks(user_id, db):
    user_with_tasks = db.query(User).filter_by(id = user_id).options(joinedload(User.tasks)).first()
    
    if not user_with_tasks:
        raise HTTPException(status_code=404, detail='Id not exists!')
    
    return user_with_tasks

def delete_user(user_id, db):
    user = get_user_or_404(user_id, db)
    
    db.query(User).filter_by(id = user_id).delete()
    
    db.commit()
    
def update_user(user_id, user_updated, db):
    user = get_user_or_404(user_id, db)
    
    email_existing = db.query(User).filter_by(email = user_updated.email).first()
    
    if email_existing and email_existing.id != user_id:
        raise HTTPException(status_code=409, detail='Email already registered!')
    
    dict_user_updated = user_updated.model_dump(exclude_unset = True)
    
    for field, value in dict_user_updated.items():
        setattr(user, field, value)
    
    db.commit()
    
    db.refresh(user)
    
    return user

def get_user_or_404(user_id, db):
    user = db.query(User).filter_by(id = user_id).first()
    
    if not user:
        raise HTTPException(status_code=404, detail='Id not exists!')
    
    return user