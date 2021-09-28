from fastapi import APIRouter

from webapp.books import route_books
from webapp.users import route_users
from webapp.auth import route_login

api_router = APIRouter()

api_router.include_router(route_books.router, prefix="", tags=["homepage"])
api_router.include_router(route_users.router, prefix="", tags=["users"])
api_router.include_router(route_login.router, prefix="", tags=["auth"])