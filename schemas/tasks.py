from pydantic import BaseModel, Field
from models.tasks import TaskStatus

class TaskBase(BaseModel):
    title: str = Field(min_length=3)
    description: str | None
    status: TaskStatus = TaskStatus.pending
    user_id: int | None = None
    
class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: str | None = Field(None, min_length = 3) 
    description: str | None = None
    status: TaskStatus | None = None
    user_id: int | None = None
    
class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    status: TaskStatus | None
    user_id: int | None

    class Config:
        from_attributes = True