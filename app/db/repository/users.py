from sqlalchemy.orm import Session

from schemas.users import CreateUser
from db.models.users import User

def create_new_user(user : CreateUser, db : Session):
    user = User(id=user.id, pw=user.pw)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user