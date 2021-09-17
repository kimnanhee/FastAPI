import datetime
from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import Date

Base = declarative_base()

class User(Base):
    __tablename__ = "book_info"
    book_no = Column(Integer, autoincrement=True)
    title = Column(String)
    price  = Column(Integer)
    publication_date = Column(Date)
    writer = Column(String)
    createtime = Column(DateTime, default=datetime.datetime.now())