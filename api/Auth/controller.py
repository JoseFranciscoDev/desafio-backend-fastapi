from fastapi import APIRouter, Depends, HTTPException
from http import HTTPStatus
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from sqlalchemy import select
from api.utils.db_services import get_db
from api._database.models import User
from api.security import verify_password
from api._shared.schemas import Token

routes = APIRouter(prefix="/auth", tags=["Auth"])


@routes.post("/token", response_model=Token)
def login_for_acess_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.scalar(select(User).where(User.email == form_data.username))
    if not user:
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED, detail="email ou senha incorretos")
    if not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED, detail="email ou senha incorretos")
    return


