from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base

DATABASE_URL = 'mysql+pymysql://root:12345r@localhost:3306/user_management_api'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = Base

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()