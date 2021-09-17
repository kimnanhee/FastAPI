import datetime
from decimal import Decimal
from sqlalchemy import Column, Integer, Numeric, String, DateTime

from db.base_class import Base

class Grade(Base):
    grade_no = Column(Integer, primary_key=True, autoincrement=True)
    user_no = Column(Integer)
    book_no = Column(Integer)
    grade = Column(Numeric)
    createtime = Column(DateTime, default=datetime.datetime.now())