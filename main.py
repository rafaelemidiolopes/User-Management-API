from models.base import Base
from database import engine
from models.tasks import Task
from models.users import User
from fastapi import FastAPI

Base.metadata.create_all(engine)
app = FastAPI()