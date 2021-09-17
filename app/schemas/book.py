from pydantic import BaseModel
from datetime import date

class CreateBook(BaseModel):
    title : str
    price : int
    publication_date : date
    writer = str

class ShowBook(BaseModel):
    title : str
    price : int
    publication_date : date
    writer = str

    class Config():
        orm_mode = True