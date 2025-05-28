from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class UserSkill(Base):
    __tablename__ = 'user_skills'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    skill_id = Column(Integer, ForeignKey('skills.id'))
    is_offering = Column(Boolean)
    is_seeking = Column(Boolean)

    user = relationship("User", back_populates="skills")
    skill = relationship("Skill", back_populates="users")
