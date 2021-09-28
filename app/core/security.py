from typing import Optional
from datetime import datetime, timedelta
import jwt 

from core.config import settings 

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    print(data)
    to_encode = data.copy()
    print(to_encode, type(to_encode))
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    print(to_encode, type(to_encode))
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt