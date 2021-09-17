from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from db.session import get_db
from db.repository.books import list_books

templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)

@router.get("/")
def home(request : Request, db : Session = Depends(get_db), msg : str = None):
    books = list_books(db = db)
    return templates.TemplateResponse("books/homepage.html", {"request":request, "jobs":books, "msg":msg})