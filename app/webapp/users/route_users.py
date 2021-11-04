from db.models.users import User
from fastapi import APIRouter, Request, Depends, responses, status
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from db.session import get_db

from webapp.users.forms import UserCreateForm
from schemas.users import CreateUser
from db.repository.users import create_new_user


templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/signup")
def signup(request: Request):
    return templates.TemplateResponse("users/signup.html", {"request": request})


@router.post("/signup")
async def signup(request: Request, db: Session=Depends(get_db)):
    form = UserCreateForm(request)
    await form.load_data()
    if await form.is_vaild():
        user = CreateUser(id=form.id, pw=form.pw)
        try:
            user = create_new_user(user=user, db=db)
            return responses.RedirectResponse("/?msg=Succesfully-Signuped", status_code=status.HTTP_302_FOUND)
        except IntegrityError:
            form.__dict__.get("errors").append("Duplicate ID")
            return templates.TemplateResponse("users/signup.html", form.__dict__)
    return templates.TemplateResponse("users/signup.html", form.__dict__)