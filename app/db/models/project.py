from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Project(Base):
    __tablename__ = "project"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(40), index=True)
    description = Column(String(40))
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="projects")