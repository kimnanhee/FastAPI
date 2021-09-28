from sqlalchemy.orm import Session

from schemas.users import CreateUser
from db.models.users import User
from core.hashing import Hasher

def create_new_user(user : CreateUser, db : Session):
    user = User(id=user.id, pw=user.pw, hashed_pw=Hasher.get_password_hash(user.pw))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user