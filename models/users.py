from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key = True)
    name = Column(String(40), nullable = False)
    email = Column(String(60), unique = True)
    
    tasks = relationship('Task', back_populates = 'user')