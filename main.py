from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from api.student_api import router as student_api_router
from routes.student_routes import router as student_routes_router
from database import engine, Base

# Jadvalni yaratish (agar mavjud bo'lmasa)
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Static fayllarni ulash
app.mount("/static", StaticFiles(directory="static"), name="static")

# Routerlarni qo‘shish
app.include_router(student_api_router)
app.include_router(student_routes_router)

