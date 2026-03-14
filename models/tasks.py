from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from models.base import Base
import enum

class TaskStatus(str, enum.Enum):
    pending = 'pending'
    in_progress = 'in_progress'
    done = 'done'
    
class Task(Base):
    __tablename__ = 'tasks'
    
    id = Column(Integer, primary_key = True)
    title = Column(String(50), nullable = False)
    description = Column(String(100))
    status = Column(Enum(TaskStatus))
    
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='tasks')