from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

conexao = 'mysql+pymysql://root:12345r@localhost:3306/user_management_api'
engine = create_engine(conexao)
Session = sessionmaker(bind = engine)

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()