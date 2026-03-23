from __future__ import annotations
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import String, ForeignKey, Enum
from models.base import Base
import enum
    
class TaskStatus(str, enum.Enum):
    pending = 'pending'
    in_progress = 'in_progress'
    done = 'done'
    
class Task(Base):
    __tablename__ = 'tasks'
    
    id: Mapped[int] = mapped_column(primary_key = True)
    title: Mapped[str] = mapped_column(String(50), nullable = False, unique = True)
    description: Mapped[str | None] = mapped_column(String(100))
    status: Mapped[TaskStatus] = mapped_column(Enum(TaskStatus))
    
    user_id: Mapped[int | None] = mapped_column(ForeignKey('users.id'))
    user: Mapped['User'] = relationship(back_populates='tasks')