from typing import Optional, List
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]

@app.get("/users", response_model=List[User])
def get_users():
    return users

@app.post("/users")
def create_user(user: User):
    users.append(user)
    return "Success" 

@app.get("/users/{id}")
def get_user(id: int=Path(..., description="User ID")):
    return users[id]

# 5:05