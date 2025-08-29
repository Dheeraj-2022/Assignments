from typing import List, Optional
from pydantic import BaseModel, Field

class ScoreBase(BaseModel):
    subject: str
    marks: float = Field(..., ge=0, le=100)

class ScoreCreate(ScoreBase):
    pass

class ScoreOut(ScoreBase):
    id: int
    class Config:
        orm_mode = True

class StudentBase(BaseModel):
    student_id: str
    name: str
    department: str

class StudentCreate(StudentBase):
    pass

class StudentOut(StudentBase):
    scores: List[ScoreOut] = []
    class Config:
        orm_mode = True
