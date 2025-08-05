from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from api.utils.db_services import get_db

routes = APIRouter(prefix="/auth", tags=["Auth"])


@routes.post("/token")
def login_for_acess_token(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_db)):
    return
