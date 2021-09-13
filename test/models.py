from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DECIMAL, VARCHAR, Date
from pydantic import BaseModel

Base = declarative_base()

class UserTable(Base):
    __tablename__ = "user_info" # 테이블 이름
    user_no = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(VARCHAR(20), unique=True, nullable=True)  
    user_pw = Column(VARCHAR(20), nullable=True)

class BookTable(Base):
    __tablename__ = "book_info" # 테이블 이름
    book_no = Column(Integer, primary_key=True, autoincrement=True)
    book_name = Column(VARCHAR(100), nullable=True)
    book_price = Column(Integer, nullable=True)
    book_date = Column(Date)
    book_writter = Column(VARCHAR(50))

class User(BaseModel):
    id: str
    pw: str

class Book(BaseModel):
    name: str
    price: int
    date: datetime
    writter: str