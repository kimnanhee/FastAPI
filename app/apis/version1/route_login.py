from datetime import timedelta
from jose import jwt, JWTError
from fastapi import APIRouter, Response, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from apis.utils import OAuth2PasswordBearerWithCookie
from sqlalchemy.orm.session import Session

from db.session import get_db
from db.repository.login import get_user
from core.hashing import Hasher
from core.security import create_access_token
from core.config import settings

router = APIRouter()

def authenticate_user(id: str, pw: str, db: Session):
    user = get_user(id=id, db=db)
    print(user)
    if not user:
        return False
    if not Hasher.verify_password(pw, user.hashed_pw):
        return False
    return user

@router.post("/token")
def login_for_access_token(response: Response, form_data: OAuth2PasswordRequestForm=Depends(), db: Session=Depends(get_db)):
    user = authenticate_user(form_data.id, form_data.pw, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    access_token_expire = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.id}, expires_delta=access_token_expire)
    response.set_cookie(key="access_token", value=f"Bearer {access_token}", httponly=True)
    return {"access_token": access_token, "token_type": "bearer"}

oauth2_scheme = OAuth2PasswordBearerWithCookie(tokenUrl="/login/token")

def get_current_user_from_token(token: str=Depends(oauth2_scheme), db: Session=Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials")
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        id: str = payload.get("sub")
        print("id is", id)
        if id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user(id=id, db=db)
    if user is None:
        raise credentials_exception
    return user
    