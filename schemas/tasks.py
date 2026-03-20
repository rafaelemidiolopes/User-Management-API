from pydantic import BaseModel, Field
from typing import Optional

class TaskBase(BaseModel):
    title: str = Field(min_length=3)
    description: Optional[str]
    status: str = 'Pending'
    user_id: int = None
    
class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    title: Optional[str]
    
class TaskResponse(TaskBase):
    id: int
    title: str
    description: str
    
    class Config:
        from_attributes = True

class TaskWithUserResponse(TaskResponse):
    id: int
    title: str
    description: str
    status: str
    user_id: int
    
    class Config:
        from_attributes = True