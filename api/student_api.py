from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Student

router = APIRouter()

# DB sessiyasini olish
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Barcha talabalarni olish
@router.get("/api/students")
def get_students(db: Session = Depends(get_db)):
    return db.query(Student).all()

# Yangi talaba qo‘shish
@router.post("/api/students/add")
def add_student(name: str, age: int, major: str, db: Session = Depends(get_db)):
    student = Student(name=name, age=age, major=major)
    db.add(student)
    db.commit()
    return {"message": "Student added successfully"}

# Talabani o‘chirish
@router.delete("/api/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if student:
        db.delete(student)
        db.commit()
        return {"message": "Student deleted"}
    return {"error": "Student not found"}
