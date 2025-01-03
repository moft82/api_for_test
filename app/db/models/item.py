from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Item(Base):
    __tablename__ = "item"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(40), index=True)
    description = Column(String(40))