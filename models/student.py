from sqlalchemy import Column, String, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship
from db import Base

class Student(Base):
    __tablename__ = "students"

    student_id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    department = Column(String)

    scores = relationship("Score", back_populates="student", cascade="all, delete")

class Score(Base):
    __tablename__ = "scores"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    subject = Column(String, index=True)
    marks = Column(Float)
    student_id = Column(String, ForeignKey("students.student_id"))

    student = relationship("Student", back_populates="scores")
