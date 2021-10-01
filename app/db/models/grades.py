import datetime
from sqlalchemy import Column, Integer, DateTime

from db.base_class import Base

class Grade(Base):
    grade_no = Column(Integer, primary_key=True, autoincrement=True)
    user_no = Column(Integer)
    book_no = Column(Integer)
    value = Column(Integer)
    createtime = Column(DateTime, default=datetime.datetime.now())