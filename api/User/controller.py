from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from api.utils.db_services import get_db
from api._shared.schemas import UserCreate, UserUpdate, UserResponse
from api.User.service import create_user, get_user, get_users, update_user, delete_user

routes = APIRouter(prefix="/user", tags=["User"])


@routes.post("/", response_model=UserResponse)
def create(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)


@routes.get("/{user_id}", response_model=UserResponse)
def read(user_id: int, db: Session = Depends(get_db)):
    return get_user(db, user_id)


@routes.get("/", response_model=List[UserResponse])
def read_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_users(db, skip, limit)


@routes.put("/{user_id}", response_model=UserResponse)
def update(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    return update_user(db, user_id, user)


@routes.delete("/{user_id}")
def delete(user_id: int, db: Session = Depends(get_db)):
    return delete_user(db, user_id)
