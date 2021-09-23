from sqlalchemy.orm import Session

from schemas.books import CreateBook
from db.models.books import Book

def create_new_book(book : CreateBook, db : Session):
    book = Book(**book.dict())
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def retreive_book(book_no: int, db : Session):
    book = db.query(Book).filter(Book.book_no == book_no).first()
    return book

def list_books(db : Session):
    books = db.query(Book).all()
    return books

def update_book_by_id(book_no: int, book: CreateBook, db: Session):
    existing_book = db.query(Book).filter(Book.book_no == book_no)
    if not existing_book.first():
        return 0
    existing_book.update(book.__dict__)
    db.commit()
    return 1

def delete_book_by_id(book_no: int, db: Session):
    existing_book = db.query(Book).filter(Book.book_no == book_no)
    if not existing_book.first():
        return 0
    existing_book.delete(synchronize_session=False)
    db.commit()
    return 1