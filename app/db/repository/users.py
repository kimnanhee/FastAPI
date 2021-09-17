from sqlalchemy.orm import Session

from schemas.users import CreateUser
from db.models.users import User

def create_new_book(user : CreateUser, db : Session):
    user = User(**user.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user