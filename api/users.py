from typing import List

from fastapi import Path, Depends, HTTPException
import fastapi
from sqlalchemy.orm import Session

from .utils.cruds import user
from schema.user import UserCreate, User
from db.db_setup import get_db

router = fastapi.APIRouter()


@router.get("/users", response_model=List[User])
def get_users(skip: int=0, limit: int=100, db: Session = Depends(get_db)):
    users = user.get_users(
        db=db,
        skip=skip,
        limit=limit
    )
    return users

# @router.post("/users")
# def create_user(user: User):
#     users.routerend(user)
#     return "Success" 

# @router.get("/users/{id}")
# def get_user(id: int=Path(..., description="User ID")):
#     return users[id]

# 5:05