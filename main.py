from fastapi import FastAPI
from db import Base, engine
from routers import student_routes

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Performance Tracker API")

# Include routes
app.include_router(student_routes.router)
