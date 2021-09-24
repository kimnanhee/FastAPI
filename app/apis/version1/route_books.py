from fastapi import APIRouter, Depends, HTTPException, status
from pydantic.errors import SequenceError
from sqlalchemy.orm import Session

from db.session import get_db
from db.models.books import Book
from schemas.books import CreateBook, ShowBook
from db.repository.books import create_new_book, retreive_book, list_books, update_book_by_id, delete_book_by_id
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
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail = f"book with No. {book_no} does not exist")
    return book

@router.get("/all", response_model=List[ShowBook])
def retreive_all_books(db : Session = Depends(get_db)):
    books = list_books(db=db)
    return books

@router.put("/update/{book_no}")
def update_book(book_no: int, book: CreateBook, db: Session=Depends(get_db)):
    book_retreive = retreive_book(book_no=book_no, db=db)
    if not book_retreive:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail = f"book with No. {book_no} does not exist")
    _ = update_book_by_id(book_no=book_no, book=book, db=db)
    return {"message":"success update data"}

@router.delete("/delete/{book_no}")
def delete_book(book_no: int, db: Session=Depends(get_db)):
    book = retreive_book(book_no=book_no, db=db)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail = f"book with No. {book_no} does not exist")
    _ = delete_book_by_id(book_no=book_no, db=db)
    return {"message":"success delete data"}