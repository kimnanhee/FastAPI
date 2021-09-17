import datetime
from decimal import Decimal
from sqlalchemy import Column, Integer, DECIMAL, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "grade_info"
    grade_no = Column(Integer, autoincrement=True)
    user_no = Column(Integer)
    book_no = Column(Integer)
    title = Column(String)
    grade = Column(Decimal(3, 1))
    createtime = Column(DateTime, default=datetime.datetime.now())