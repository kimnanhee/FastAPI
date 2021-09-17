from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from db.session import engine
from db.base import Base
from apis.base import api_router
from webapp.base import api_router as webapp_router


def create_tables():
    Base.metadata.create_all(bind=engine)


def include_router(app):
    app.include_router(api_router)
    app.include_router(webapp_router)


def start_application():
    app = FastAPI(title="NH recommand", version="0.0.1")
    create_tables()
    include_router(app)
    return app


app = start_application()