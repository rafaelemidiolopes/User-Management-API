from pydantic import EmailStr, BaseModel, Field
from typing import Optional, List
from tasks import TaskResponse

class UserBase(BaseModel):
    name: str = Field(min_length=3)
    email: EmailStr
    
class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    
class UserResponse(UserBase):
    class Config:
        from_atributes = True
        
class UserWithTasksResponse(UserResponse):
    tasks: List[TaskResponse]