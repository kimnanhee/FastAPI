import datetime
from sqlalchemy import Column, Integer, String, DateTime

from db.base_class import Base

class User(Base):
    user_no = Column(Integer, primary_key=True, autoincrement=True)
    id = Column(String(50), unique=True)
    pw = Column(String(50))
    createtime = Column(DateTime, default=datetime.datetime.now())