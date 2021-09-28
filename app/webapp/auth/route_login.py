from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from db.session import get_db

from webapp.auth.forms import LoginForm
from apis.version1.route_login import login_for_access_token


templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/login")
def login(request : Request):
    return templates.TemplateResponse("auth/login.html", {"request": request})


@router.post("/login")
async def login(request : Request, db: Session=Depends(get_db)):
    form = LoginForm(request)
    await form.load_data()
    if await form.is_vaild():
        try:
            form.__dict__.update(msg="Login Successful :)")
            response = templates.TemplateResponse("auth/login.html", form.__dict__)
            login_for_access_token(response=response, form_data=form, db=db)
            return response
        except HTTPException:
            form.__dict__.update(msg="")
            form.__dict__.get("errors").append("Incorrect id or password")
            return templates.TemplateResponse("auth/login.html",form.__dict__)
    return templates.TemplateResponse("auth/login.html", form.__dict__)