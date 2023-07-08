from typing import Optional, List
from fastapi import FastAPI, Path
from pydantic import BaseModel

from api.users import router as _users
from api.sections import router as _sections
from api.courses import router as _courses

from db.db_setup import engine
from db.models import user, course

user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(_users)
app.include_router(_sections)
app.include_router(_courses)

# 1:42