from sqlalchemy.orm import Session

from db.models import user
from schema import user as _user

def get_user(db: Session, user_id: int):
    return db.query(user.User).filter(user.User.id == user_id).first()

def get_user_by_email(db: Session, email:str):
    return db.query(user.User).filter(user.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(user.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: _user.UserCreate):
    db_user = user.User(email=user.email, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
    