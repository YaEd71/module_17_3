from fastapi import FastAPI
from sqlalchemy.orm import Session
from app.models import Task, User
from app.backend.db import Base, engine, SessionLocal

app = FastAPI()

import logging

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

# Создание таблиц
Base.metadata.create_all(bind=engine)


# Зависимость для получения сессии
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# При запуске приложения через main.py будут автоматически созданы таблицы tasks и users в базе данных taskmanager.db