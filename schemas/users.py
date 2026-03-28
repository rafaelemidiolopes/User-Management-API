from pydantic import EmailStr, BaseModel, Field, ConfigDict
from schemas.tasks import TaskResponse

class UserBase(BaseModel):
    name: str = Field(min_length=3)
    email: EmailStr
    
class UserCreate(UserBase):
    password: str = Field(min_length=6)

class UserUpdate(BaseModel):
    name: str | None = Field(default = None, min_length = 3)
    email: EmailStr | None = None
    
class UserResponse(UserBase):
    id: int
    
    model_config = ConfigDict(from_attributes = True)
        
class UserWithTasksResponse(UserResponse):
    tasks: list[TaskResponse]
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str