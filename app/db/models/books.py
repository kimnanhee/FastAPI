import datetime
from sqlalchemy import Column, Integer, String, Date, DateTime

from db.base_class import Base

class Book(Base):
    book_no = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100))
    price  = Column(Integer)
    publication_date = Column(Date)
    writer = Column(String(50))
    createtime = Column(DateTime, default=datetime.datetime.now())