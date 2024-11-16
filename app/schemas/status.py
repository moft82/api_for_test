from pydantic import BaseModel

class StatusBase(BaseModel):
    name: str
    code: int
    status: str
    

class StatusCreate(StatusBase):
    pass

class Status(StatusBase):
    id: int

    class Config:
        from_orm = True