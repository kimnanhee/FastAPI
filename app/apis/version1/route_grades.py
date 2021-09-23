from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.session import get_db
from db.models.grades import Grade
from schemas.grades import CreateGrade, ShowGrade
from db.repository.grades import create_new_grade, retreive_grade, list_grade, update_grade_by_id, delete_grade_by_id
from typing import List

router = APIRouter()

@router.post("/create-grade", response_model=ShowGrade)
def create_grade(grade: CreateGrade, db: Session=Depends(get_db)):
    grade = create_new_grade(grade=grade, db=db)
    return grade

@router.get("/get/{grade_no}", response_model=ShowGrade)
def retreive_grade_by_id(grade_no: int, db: Session=Depends(get_db)):
    grade = retreive_grade(grade_no=grade_no, db=db)
    print(grade)
    if not grade:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail = f"grade with id {id} does not exist")
    return grade

@router.get("/get/all", response_model=List[ShowGrade])
def retreive_all_grades(db: Session=Depends(get_db)):
    grades = list_grade(db=db)
    return grades

@router.put("/update/{grade_no}")
def update_grade(grade_no: int, grade: CreateGrade, db: Session=Depends(get_db)):
    grade_retreive = retreive_grade(grade_no=grade_no, db=db)
    if not grade_retreive:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail = f"grade with id {id} does not exist")
    _ = update_grade_by_id(grade_no=grade_no, grade=grade, db=db)
    return {"message":"success update grade"}

@router.delete("/delete/{grade_no}")
def delete_grade(grade_no: int, db: Session=Depends(get_db)):
    grade_retreive = retreive_grade(grade_no=grade_no, db=db)
    if not grade_retreive:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail = f"grade with id {id} does not exist")
    _ = delete_grade_by_id(grade_no=grade_no, db=db)
    return {"message":"success delete grade"}