from pydantic import BaseModel

class CreateGrade(BaseModel):
    user_no : int
    book_no : int
    grade : int

class ShowGrade(BaseModel):
    user_no : int
    book_no : int
    grade : int

    class Config():
        orm_mode = True