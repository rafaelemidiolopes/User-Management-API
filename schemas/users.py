from pydantic import EmailStr, BaseModel, Field, ConfigDict
from typing import List
from schemas.tasks import TaskResponse

class UserBase(BaseModel):
    name: str = Field(min_length=3)
    email: EmailStr
    
class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    name: str | None = Field(default = None, min_length = 3)
    email: EmailStr | None = None
    
class UserResponse(UserBase):
    id: int
    
    model_config = ConfigDict(from_attributes = True)
        
class UserWithTasksResponse(UserResponse):
    tasks: List[TaskResponse]