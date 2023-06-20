from typing import Optional, List
from fastapi import FastAPI, Path
import fastapi
from pydantic import BaseModel

router = fastapi.APIRouter()

users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]

@router.get("/users", response_model=List[User])
def get_users():
    return users

@router.post("/users")
def create_user(user: User):
    users.routerend(user)
    return "Success" 

@router.get("/users/{id}")
def get_user(id: int=Path(..., description="User ID")):
    return users[id]

# 5:05