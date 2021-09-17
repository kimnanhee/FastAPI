# 3개의 DB 모델을 import
from db.base_class import Base
from db.models.users import User
from db.models.books import Book
from db.models.grades import Grade