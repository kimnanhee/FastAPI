from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from db.session import engine
from db.base import Base

def create_tables():
    Base.metadata.create_all(bind=engine)

def start_application():
    app = FastAPI()
    create_tables()
    return app

app = start_application()