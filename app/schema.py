from sqlalchemy import Column, DECIMAL, Integer, VARCHAR, Date, DateTime
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.functions import now

Base = declarative_base()

class UserTable(Base):
    __tablename__ = "user_info" # 테이블 이름
    user_no = Column(Integer, primary_key=True, autoincrement=True)
    id = Column(VARCHAR(50))  
    pw = Column(VARCHAR(50))
    createtime = Column(DateTime, default=now())

class BookTable(Base):
    __tablename__ = "book_info" # 테이블 이름
    book_no = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(VARCHAR(100))
    price = Column(Integer)
    publication_date = Column(Date)
    writer = Column(VARCHAR(50))
    createtime = Column(DateTime, default=now())

class GradeTable(Base):
    __tablename__ ="grade_info" # 테이블 이름
    grade_no = Column(Integer, primary_key=True, autoincrement=True)
    user_no = Column(Integer)
    book_no = Column(Integer)
    grade = Column(DECIMAL(3, 1))
    createtime = Column(DateTime, default=now())