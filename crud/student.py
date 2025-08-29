from sqlalchemy.orm import Session
from models.student import Student, Score
from schemas.student import StudentCreate, ScoreCreate
from sqlalchemy import func

def create_student(db: Session, student: StudentCreate):
    db_student = Student(student_id=student.student_id, name=student.name, department=student.department)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_students(db: Session):
    return db.query(Student).all()

def get_student(db: Session, student_id: str):
    return db.query(Student).filter(Student.student_id == student_id).first()

def delete_student(db: Session, student_id: str):
    db_student = get_student(db, student_id)
    if db_student:
        db.delete(db_student)
        db.commit()
        return True
    return False

def search_students(db: Session, name: str):
    return db.query(Student).filter(Student.name.ilike(f"%{name}%")).all()

def add_score(db: Session, student_id: str, score: ScoreCreate):
    student = get_student(db, student_id)
    if not student:
        return None
    existing = db.query(Score).filter(Score.student_id == student_id, Score.subject == score.subject).first()
    if existing:
        existing.marks = score.marks
        db.commit()
        db.refresh(existing)
        return existing
    db_score = Score(subject=score.subject, marks=score.marks, student_id=student_id)
    db.add(db_score)
    db.commit()
    db.refresh(db_score)
    return db_score

def get_average_score(db: Session, student_id: str):
    scores = db.query(Score).filter(Score.student_id == student_id).all()
    if not scores:
        return 0.0
    return sum(s.marks for s in scores) / len(scores)

def get_top_scorer(db: Session, subject: str):
    return db.query(Student).join(Score).filter(Score.subject == subject).order_by(Score.marks.desc()).first()

def get_department_average(db: Session, department: str):
    students = db.query(Student).filter(Student.department == department).all()
    if not students:
        return 0.0
    averages = [get_average_score(db, s.student_id) for s in students if s.scores]
    return sum(averages) / len(averages) if averages else 0.0
