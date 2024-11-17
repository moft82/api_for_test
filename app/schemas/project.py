from typing import Optional
from pydantic import BaseModel

class ProjectBase(BaseModel):
    title: str
    description: str

class ProjectCreate(ProjectBase):
    user_id:int

class ProjectUpdate(ProjectBase):
    title: Optional[str] = None
    description: Optional[str] = None

class ProjectResponse(ProjectBase):
    id: int
    user_id: int

    class Config:
        from_orm = True