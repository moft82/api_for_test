from typing import Optional
from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    description: str

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    name: Optional[str] = None
    description: Optional[str] = None


class ItemResponse(ItemBase):
    id: int

    class Config:
        from_orm = True
