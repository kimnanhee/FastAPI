import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "user_info"
    user_no = Column(Integer, autoincrement=True)
    id = Column(String)
    pw = Column(String)
    createtime = Column(DateTime, default=datetime.datetime.now())