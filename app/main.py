from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import sqlalchemy as db

metadata = db.MetaData()
user_info = db.Table('user_info', metadata, autoload_with=engine)

 
app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def root():
    return templates("login.html")

@app.post("/signin")
async def signin(id: str, pw: str):
    if ' ' in id or ' ' in pw:
        return {"message": "아이디나 비밀번호에 공백이 포함"}
    
    ResultProxy = connection.execute("SELECT pw FROM user_info WHERE id='%s'" % (id))
    ResultSet = ResultProxy.fetchone()

    if not ResultSet:
        return {"message": "아이디를 찾을 수 없습니다"}
    elif ResultSet[0] != pw:
        return {"message": "비밀번호가 틀렸습니다"}
    else:
        return {"message": "로그인에 성공하셨습니다"}


@app.post("/signup")
async def signup(id: str, pw: str):
    if ' ' in id or ' ' in pw:
        return {"message": "아이디나 비밀번호에 공백이 포함"}

    ResultProxy = connection.execute("SELECT pw FROM user_info WHERE id='%s'" % (id))
    ResultSet = ResultProxy.fetchone()

    if ResultSet:
        return {"message": "아이디가 이미 있습니다"}
    
    connection.execute("INSERT INTO user_info(id, pw, createtime) VALUES(\"%s\", \"%s\", now())" % (id, pw))
    return {"message": "회원가입에 성공하셨습니다"}


@app.get("/book")
async def list(book_start: int = 0, book_end: int = 20, order: str = "book_no"):
    ResultProxy = connection.execute("SELECT * FROM book_info WHERE %d <= book_no <= %d ORDER BY %s" % (book_start, book_end, order))
    ResultSet = ResultProxy.fetchall()
    return ResultSet


@app.get("/book/{book_no}")
async def list(book_no: int):
    ResultProxy = connection.execute("SELECT * FROM book_info WHERE book_no = %d" % (book_no))
    ResultSet = ResultProxy.fetchone()
    if not ResultSet:
        return {"message": "도서를 찾을 수 없습니다"}
    return ResultSet


@app.post("/grade")
async def grade(user_no: int, book_no: int, grade: float):
    ResultProxy = connection.execute("SELECT * FROM grade_info WHERE user_no = %d AND book_no = %d" % (user_no, book_no))
    ResultSet = ResultProxy.fetchone()
    if ResultSet:
        connection.execute("UPDATE grade_info SET grade = %.1f WHERE user_no = %d AND book_no = %d" % (grade, user_no, book_no))
        return {"message" : "평점을 변경하는데 성공하셨습니다"}

    connection.execute("INSERT INTO grade_info(user_no, book_no, grade) VALUES(%d, %d, %.1f)" % (user_no, book_no, grade))
    return {"message" : "평점을 메기는데 성공하셨습니다"}

'''
# select
query = db.select([user_info])
ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
print(ResultSet)

# where
query = db.select([user_info]).where(user_info.columns.id == "ju")
ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
print(ResultSet)

# order by
query = db.select([user_info]).order_by(db.desc(user_info.columns.id))
ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
print(ResultSet)

# add
# query = db.add
ResultProxy = connection.execute("SELECT * FROM %s" % ("user_info"))
ResultSet = ResultProxy.fetchall()
print(ResultProxy, type(ResultProxy), ResultSet, type(ResultSet))
'''