from fastapi import HTTPException
from models.users import User
from sqlalchemy.orm import selectinload, joinedload