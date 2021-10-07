from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import and_
from sqlalchemy.sql.functions import user

from schemas.grades import CreateGrade
from db.models.grades import Grade
from db.repository.books import list_books

def create_new_grade(grade: CreateGrade, db: Session):
    existing_grade = db.query(Grade).filter((Grade.user_no == grade.user_no) & (Grade.book_no == grade.book_no)).first()
    if existing_grade:
        db.query(Grade).filter((Grade.user_no == grade.user_no) & (Grade.book_no == grade.book_no)).update({"value": grade.value})
        db.commit()
        return 0
    else:
        grade = Grade(user_no=grade.user_no, book_no=grade.book_no, value=grade.value)
        db.add(grade)
        db.commit()
        db.refresh(grade)
        return grade

def retreive_grade(grade_no: int, db: Session):
    grade = db.query(Grade).filter(Grade.grade_no == grade_no).first()
    return grade

def list_grade(db: Session):
    grades = db.query(Grade).all()
    return grades

def reco(user_no: int, db: Session):
    user_rating_books = db.query(Grade.book_no).filter(Grade.user_no == user_no).all() # 사용자가 평가한 책 번호 가져오기
    user_rating_books = [i[0] for i in user_rating_books]

    books = list_books(db=db)
    if user_rating_books == books:
        return False
    arr = []
    for book in books:
        if not book.book_no in user_rating_books:
            arr.append(book.book_no)
    return arr

def update_grade_by_id(grade_no: int, grade: CreateGrade, db: Session):
    existing_grade = db.query(Grade).filter(Grade.grade_no == grade_no)
    if not existing_grade.first():
        return 0
    existing_grade.update(grade.__dict__)
    db.commit()
    return 1

def delete_grade_by_id(grade_no: int, db: Session):
    existing_grade = db.query(Grade).filter(Grade.grade_no == grade_no)
    if not existing_grade.first():
        return 0
    existing_grade.delete(synchronize_session=False)
    db.commit()
    return 1