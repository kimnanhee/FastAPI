from fastapi import APIRouter

from webapp.books import route_books

api_router = APIRouter()

api_router.include_router(route_books.router, prefix="", tags=["homepage"])