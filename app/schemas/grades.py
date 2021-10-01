from pydantic import BaseModel

class CreateGrade(BaseModel):
    user_no : int
    book_no : int
    value : int

class ShowGrade(BaseModel):
    user_no : int
    book_no : int
    value : int

    class Config():
        orm_mode = True