from fastapi import APIRouter, Response
from sqlalchemy.orm import session
from sqlalchemy.orm.session import Session
from db.session import get_db
from db.repository.login import get_user

router = APIRouter()

def authenticate_user(id: str, pw: str, db: Session):
    user = get_user(id=id, db=db)
    print(user)
    if not user:
        return False
    return user

@router.post("/create_session/{id}")
async def create_session(id: str, reponse: Response):
    return {"message": "hello"}