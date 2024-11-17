from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from app.db.database import Base

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    name = Column(String(50), index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    projects = relationship("Project", back_populates="user")