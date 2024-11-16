from pydantic import BaseModel, EmailStr
from app.schemas.item import Item

class UserBase(BaseModel):
    pass

class UserCreate(UserBase):
    email: EmailStr
    password: str
    pass

class User(UserBase):
    items: list[Item] = []

    class Config:
        from_orm = True