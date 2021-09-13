from fastapi import FastAPI
from pydantic import BaseModel

from models import UserTable, User
from db import ses

app = FastAPI()

class User(BaseModel):
    id: str
    pw: str

@app.get("/")
def root():
    return {"hello":"world"}

@app.post("/signin")
def signin(id: str, pw: str):
    user = UserTable()
    user.user_id, user.user_pw = id, pw

    ses.add(user)
    ses.commit()
    
    return {"id":user}