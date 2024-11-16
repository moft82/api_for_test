from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from app.db.database import Base

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    email = Column(String(50), unique=True, index=True, nullable=False)
    password = Column(String(50), nullable=False)
    items = relationship("Item", back_populates="user")
    