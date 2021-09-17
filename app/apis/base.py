from fastapi import APIRouter

from apis.version1 import route_books

api_router = APIRouter()

api_router.include_router(route_books.router, prefix="/books", tags=["books"])