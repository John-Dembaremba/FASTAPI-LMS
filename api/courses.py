from typing import Optional, List
from fastapi import FastAPI, Path
import fastapi
from pydantic import BaseModel

router = fastapi.APIRouter()

@router.get("/courses")
def create_course():
    return {"courses": []}

@router.get("/courses")
def read_courses():
    return {"courses": []}

@router.get("/course/{id}/detail")
def read_course():
    return {"course": []}

@router.get("/course/{id}/update")
def update_course():
    return {"course": []}

@router.get("/course/{id}/delete")
def delete_course():
    return {"course": []}

