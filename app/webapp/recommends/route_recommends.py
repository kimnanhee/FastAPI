from fastapi import APIRouter, Request, Depends, responses, status
from fastapi.templating import Jinja2Templates
from fastapi.security.utils import get_authorization_scheme_param
from sqlalchemy.orm import Session
import xlearn, pandas

from apis.version1.route_login import get_current_user_from_token

from db.session import get_db
from db.models.users import User
from db.repository.grades import reco
from db.repository.books import retreive_book


templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/recommend/")
def recommend(request: Request, db: Session=Depends(get_db)):
    try:
        token = request.cookies.get("access_token")
        sheme, param = get_authorization_scheme_param(token)
        current_user: User = get_current_user_from_token(token=param, db=db)
        books = reco(user_no=current_user.user_no, db=db) # 평가하지 않은 책의 번호
        print("books - ", books)
        if books:            
            grade_test = pandas.DataFrame({"value": [0 for _ in range(len(books))], "user_no": [current_user.user_no for _ in range(len(books))], "book_no": books})
            grade_test = pandas.get_dummies(data=grade_test, columns=["user_no", "book_no"], prefix=["user_no", "book_no"])

            # get test x, y
            test_x = grade_test[grade_test.columns[1:]]
            test_y = grade_test[grade_test.columns[0]]
            xdm_test = xlearn.DMatrix(test_x, test_y)

            fm_model = xlearn.create_fm()
            fm_model.setTest(xdm_test)
            result = fm_model.predict("./xlearn_test/out/model.out")
            print(result)

            book_list = [[((result[i]*100)//1)/5, retreive_book(book_no=book_no, db=db)] for i, book_no in enumerate(books)]
            book_list.sort(key=lambda x: -x[0])
            print(book_list)
            return templates.TemplateResponse("books/show_books_to_recommend.html", {"request": request, "books": book_list})

        else: # 모든 책에 평점을 메김
            return templates.TemplateResponse("books/show_books_to_recommend.html", {"request": request, "errors": ["You have rated all books. If other books are added, I will recommend them!!"]})
    except Exception as e:
        print(e)
        return templates.TemplateResponse("books/show_books_to_recommend.html", {"request": request, "errors": ["You might not be logged in, In case problem persists please contact us."]})
    