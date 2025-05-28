from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Skill(Base):
    __tablename__ = 'skills'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)

    users = relationship("UserSkill", back_populates="skill")
