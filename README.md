# Student Performance Tracker – FastAPI + SQLite

This is the REST API implementation of the Student Performance Tracker.

## Features

- Add, list, get, delete students
- Search students by name
- Add/update subject scores
- Get average score per student
- Get top scorer per subject
- Get department average score

## Tech Stack

- FastAPI
- SQLite (switchable to PostgreSQL)
- SQLAlchemy ORM
- Pydantic models

## How to Run

```bash
pip install fastapi uvicorn sqlalchemy
uvicorn main:app --reload
```

Visit Swagger UI at: http://127.0.0.1:8000/docs

## Endpoints

- POST /students/
- GET /students/
- GET /students/{student_id}
- DELETE /students/{student_id}
- GET /students/search/?name=Alice
- POST /students/{student_id}/scores/
- GET /students/{student_id}/average-score/
- GET /students/top-scorer/{subject}
- GET /departments/{department}/average-score/
