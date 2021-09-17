from fastapi import APIRouter, Depends
from pydantic.errors import SequenceError
from sqlalchemy.orm import Session

from db.session import get_db
from db.models.books import Book
from db.repository.books import create_new_book, retreive_book, list_books
from schemas.books import CreateBook, ShowBook
from db.models.users import User
from typing import List

router = APIRouter()

@router.post("/create-book", response_model=ShowBook)
def create_book(book : CreateBook, db : Session = Depends(get_db)):
    book = create_new_book(book=book, db=db)
    return book

@router.get("/get/{book_no}", response_model=ShowBook)
def retreive_book_by_id(book_no : int, db : Session = Depends(get_db)):
    book = retreive_book(book_no=book_no, db=db)
    print(book)
    if not book:
        return f"book with id {id} does not exist"
    return book

@router.get("/all", response_model=List[ShowBook])
def retreive_all_books(db : Session = Depends(get_db)):
    books = list_books(db=db)
    return books