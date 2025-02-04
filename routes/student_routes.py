from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Student

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# DB sessiyasini olish
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 🏠 Asosiy sahifani /students sahifasiga yo‘naltirish
@router.get("/", response_class=RedirectResponse)
def home():
    return RedirectResponse(url="/students", status_code=303)

# 📌 Barcha talabalarni ko‘rsatish (students.html sahifasi)
@router.get("/students", response_class=HTMLResponse)
def get_students_page(request: Request):
    db = SessionLocal()
    students = db.query(Student).all()
    db.close()
    return templates.TemplateResponse("students.html", {"request": request, "students": students})

# ➕ Yangi talaba qo‘shish
@router.post("/students/add", response_class=RedirectResponse)
def add_student(name: str = Form(...), age: int = Form(...), major: str = Form(...)):
    db = SessionLocal()
    new_student = Student(name=name, age=age, major=major)
    db.add(new_student)
    db.commit()
    db.close()
    return RedirectResponse(url="/students", status_code=303)

# ✏️ Talabani tahrirlash sahifasi (edit_student.html)
@router.get("/students/edit/{student_id}", response_class=HTMLResponse)
def edit_student_page(student_id: int, request: Request):
    db = SessionLocal()
    student = db.query(Student).filter(Student.id == student_id).first()
    db.close()
    if not student:
        return RedirectResponse(url="/students", status_code=303)
    return templates.TemplateResponse("edit_student.html", {"request": request, "student": student})

# 🔄 Talabani yangilash
@router.post("/students/edit/{student_id}", response_class=RedirectResponse)
def update_student(student_id: int, name: str = Form(...), age: int = Form(...), major: str = Form(...)):
    db = SessionLocal()
    student = db.query(Student).filter(Student.id == student_id).first()
    if student:
        student.name = name
        student.age = age
        student.major = major
        db.commit()
    db.close()
    return RedirectResponse(url="/students", status_code=303)

# ❌ Talabani o‘chirish
@router.post("/students/delete/{student_id}", response_class=RedirectResponse)
def delete_student(student_id: int):
    db = SessionLocal()
    student = db.query(Student).filter(Student.id == student_id).first()
    if student:
        db.delete(student)
        db.commit()
    db.close()
    return RedirectResponse(url="/students", status_code=303)

# ℹ️ About sahifasi (about.html)
@router.get("/about", response_class=HTMLResponse)
def about_page(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})
