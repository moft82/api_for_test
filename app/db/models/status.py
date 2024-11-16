from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Status(Base):
    __tablename__ = "status"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(40))
    code = Column(Integer)
    status = Column(String(40))