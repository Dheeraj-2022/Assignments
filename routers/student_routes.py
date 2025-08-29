from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import SessionLocal
from schemas.student import StudentCreate, StudentOut, ScoreCreate
from crud import student as crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/students/", response_model=StudentOut)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student.student_id)
    if db_student:
        raise HTTPException(status_code=400, detail="Student already exists")
    return crud.create_student(db, student)

@router.get("/students/", response_model=list[StudentOut])
def list_students(db: Session = Depends(get_db)):
    return crud.get_students(db)

@router.get("/students/{student_id}", response_model=StudentOut)
def get_student(student_id: str, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id)
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@router.delete("/students/{student_id}")
def delete_student(student_id: str, db: Session = Depends(get_db)):
    success = crud.delete_student(db, student_id)
    if not success:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"detail": "Student deleted successfully"}

@router.get("/students/search/")
def search_students(name: str, db: Session = Depends(get_db)):
    return crud.search_students(db, name)

# Scores endpoints
@router.post("/students/{student_id}/scores/")
def add_score(student_id: str, score: ScoreCreate, db: Session = Depends(get_db)):
    s = crud.add_score(db, student_id, score)
    if not s:
        raise HTTPException(status_code=404, detail="Student not found")
    return s

@router.get("/students/{student_id}/average-score/")
def average_score(student_id: str, db: Session = Depends(get_db)):
    return {"average": crud.get_average_score(db, student_id)}

@router.get("/students/top-scorer/{subject}")
def top_scorer(subject: str, db: Session = Depends(get_db)):
    s = crud.get_top_scorer(db, subject)
    if not s:
        raise HTTPException(status_code=404, detail="No scores found for this subject")
    return {"student_id": s.student_id, "name": s.name, "marks": max(sc.marks for sc in s.scores if sc.subject == subject)}

@router.get("/departments/{department}/average-score/")
def dept_average(department: str, db: Session = Depends(get_db)):
    avg = crud.get_department_average(db, department)
    return {"average": avg}
