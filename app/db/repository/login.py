from sqlalchemy.orm import Session
from db.models.users import User

def get_user(id : str, db : Session):
    user = db.query(User).filter(User.id == id).first()
    return user