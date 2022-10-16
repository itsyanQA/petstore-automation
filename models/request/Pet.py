from typing import Optional
from pydantic import BaseModel
from models.enum.Category import Category
from models.enum.Status import Status
from models.enum.Tag import Tag


class Pet(BaseModel):
    id: Optional[int] = None
    category: Optional[Category] = None
    name: str = None
    photoUrls: list[str] = None
    tags: Optional[Tag] = None
    status: Optional[Status] = None


class CustomStatusPet(BaseModel):
    id: Optional[int] = None
    category: Optional[Category] = None
    name: str = None
    photoUrls: list[str] = None
    tags: Optional[Tag] = None
    status: Optional[str] = None

