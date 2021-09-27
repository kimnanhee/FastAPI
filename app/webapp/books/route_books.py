from fastapi import APIRouter, Request, Depends, responses, status
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from typing import Optional
from db.session import get_db
from db.repository.books import list_books, list_books_name, retreive_book

from webapp.books.forms import BookCreateForm
from schemas.books import CreateBook
from db.repository.books import create_new_book


templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/")
def home(request : Request, db : Session = Depends(get_db), msg : str = None):
    books = list_books(db = db)
    return templates.TemplateResponse("books/homepage.html", {"request": request, "books": books, "msg": msg})


@router.get("/detail/{book_no}")
def book_detail(book_no: int, request: Request, db: Session=Depends(get_db)):
    book = retreive_book(book_no=book_no, db=db)
    return templates.TemplateResponse("books/detail.html", {"request": request, "book": book})


@router.get("/post-a-book/")
def create_job(request: Request, db: Session=Depends(get_db)):
    return templates.TemplateResponse("books/create_book.html", {"request": request})


@router.post("/post-a-book/")
async def create_job(request: Request, db: Session=Depends(get_db)):
    form = BookCreateForm(request)
    await form.load_data()
    if await form.is_vaild():
        try:
            book = CreateBook(**form.__dict__)
            book = create_new_book(book=book, db=db)
            return responses.RedirectResponse(f"/detail/{book.book_no}", status_code=status.HTTP_302_FOUND)
        except Exception as e:
            print(e)
            return templates.TemplateResponse("books/create_book.html", form.__dict__)
    return templates.TemplateResponse("books/create_book.html", form.__dict__)


@router.get("/delete-book/")
def show_books_to_delete(request: Request, db: Session=Depends(get_db)):
    books = list_books(db=db)
    return templates.TemplateResponse("books/show_books_to_delete.html", {"request": request, "books": books})


@router.get("/search")
def search(request: Request, db: Session=Depends(get_db), q: Optional[str]=None):
    books = list_books_name(title=q, db=db)
    return templates.TemplateResponse("books/show_books_to_search.html", {"request": request, "books": books})