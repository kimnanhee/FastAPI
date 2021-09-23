from fastapi import APIRouter

from apis.version1 import route_users
from apis.version1 import route_books
from apis.version1 import route_login
from apis.version1 import route_grades

api_router = APIRouter()

api_router.include_router(route_users.router, prefix="/users", tags=["users"])
api_router.include_router(route_books.router, prefix="/books", tags=["books"])
api_router.include_router(route_login.router, prefix="/login", tags=["login"])
api_router.include_router(route_grades.router, prefix="/grades", tags=["grades"])