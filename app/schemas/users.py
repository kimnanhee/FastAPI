from pydantic import BaseModel

class CreateUser(BaseModel):
    id : str
    pw : str

class ShowUser(BaseModel):
    id : str

    class Config():
        orm_mode = True