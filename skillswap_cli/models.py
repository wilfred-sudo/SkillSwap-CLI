from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    contact = Column(String)

    skills = relationship("Skill", back_populates="user")
    taught_sessions = relationship("Session", back_populates="teacher", foreign_keys='Session.teacher_id')
    learned_sessions = relationship("Session", back_populates="learner", foreign_keys='Session.learner_id')

class Skill(Base):
    __tablename__ = 'skills'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="skills")
    sessions = relationship("Session", back_populates="skill")

class Session(Base):
    __tablename__ = 'sessions'

    id = Column(Integer, primary_key=True)
    skill_id = Column(Integer, ForeignKey('skills.id'))
    teacher_id = Column(Integer, ForeignKey('users.id'))
    learner_id = Column(Integer, ForeignKey('users.id'))
    notes = Column(String)

    skill = relationship("Skill", back_populates="sessions")
    teacher = relationship("User", back_populates="taught_sessions", foreign_keys=[teacher_id])
    learner = relationship("User", back_populates="learned_sessions", foreign_keys=[learner_id])