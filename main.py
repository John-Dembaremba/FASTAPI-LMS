from typing import Optional, List
from fastapi import FastAPI, Path
from pydantic import BaseModel
from api.users import router

app = FastAPI()

app.include_router(router)