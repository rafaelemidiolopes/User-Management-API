from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

conexao = 'mysql+pymysql://root:12345r@localhost:3306/user_management_api'

engine = create_engine(conexao)

Session = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = declarative_base()

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()