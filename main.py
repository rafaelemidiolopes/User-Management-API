from database import engine
from fastapi import FastAPI
from routers.users import router as users_router
from routers.tasks import router as tasks_router
from models.users import User
from models.tasks import Task
from models.base import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users_router)
app.include_router(tasks_router)