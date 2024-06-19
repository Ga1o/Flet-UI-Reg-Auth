from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
import os


DB_FILE_PATH = 'db/data.db'
os.makedirs(os.path.dirname(DB_FILE_PATH), exist_ok=True)
DB_URL = f'sqlite:///{DB_FILE_PATH}'
engine = create_engine(DB_URL, echo=True)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(50))
    user_email = Column(String(100), unique=True)
    user_password = Column(String(256))
    created = Column(DateTime, default=datetime.now)


Base.metadata.create_all(engine)

# Создание сессии для работы с базой данных
Session = sessionmaker(bind=engine)
session = Session()
