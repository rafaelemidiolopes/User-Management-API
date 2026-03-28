from __future__ import annotations
from sqlalchemy import String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from models.base import Base

class User(Base):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(String(40))
    email: Mapped[str] = mapped_column(String(60), unique = True)
    password_hash: Mapped[str] = mapped_column(String(255))
    
    tasks: Mapped[list['Task']] = relationship(back_populates = 'user')