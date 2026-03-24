from pydantic import EmailStr, BaseModel, Field
from typing import List
from schemas.tasks import TaskResponse

class UserBase(BaseModel):
    name: str = Field(min_length=3)
    email: EmailStr
    
class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    name: str = None
    email: EmailStr = None
    
class UserResponse(BaseModel):
    id: int
    name: str = Field(min_length=3)
    email: EmailStr
    
    class Config:
        from_attributes = True
        
class UserWithTasksResponse(UserResponse):
    tasks: List[TaskResponse]