from database import engine, Base
from fastapi import FastAPI
from routers import users, tasks

app = FastAPI()

Base.metadata.create_all(engine)

app.include_router(users.router)
app.include_router(tasks.router)