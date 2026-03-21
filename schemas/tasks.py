from pydantic import BaseModel, Field
from typing import Optional

class TaskBase(BaseModel):
    title: str = Field(min_length=3)
    description: Optional[str]
    status: str = 'Pending'
    user_id: int = None
    
class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: str | None = Field(None, min_length = 3) 
    description: str = None
    status: str = None
    user_id: int = None
    
class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    status: str | None
    user_id: int | None

    class Config:
        from_attributes = True