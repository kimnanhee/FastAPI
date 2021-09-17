# DB에 연결하고, 세션을 생성

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from typing import Generator

engine = create_engine("mysql+mysqldb://root:chun0225!@127.0.0.1:3306/test?charset=utf8", encoding="utf-8",  convert_unicode=False)

SessionLocal = sessionmaker(autocommit=False, bind=engine)

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()