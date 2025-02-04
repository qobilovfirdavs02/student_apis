# Student Management System (FastAPI + MySQL)

This is a simple **Student Management System** built using **FastAPI** with **MySQL** database integration. The application allows users to **add, edit, delete, and view students** using a web interface.

---

## 📌 Features
- FastAPI-based web application
- MySQL database integration
- Jinja2 templates for frontend rendering
- RESTful API for managing students
- Styled with CSS for a better UI/UX

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2️⃣ Create and Activate a Virtual Environment
```sh
python -m venv venv
```
- **Windows:**
  ```sh
  venv\Scripts\activate
  ```
- **Mac/Linux:**
  ```sh
  source venv/bin/activate
  ```

### 3️⃣ Install Required Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Set Up MySQL Database

#### ➜ Create a MySQL Database
Login to MySQL and create a new database:
```sql
CREATE DATABASE student_db;
```

#### ➜ Configure Database Connection
Modify `config.py` or `.env` file with your **MySQL credentials**:
```python
DATABASE_URL = "mysql+pymysql://username:password@localhost/student_db"
```

### 5️⃣ Run Database Migrations
If using **SQLAlchemy & Alembic**, apply migrations:
```sh
alembic upgrade head
```

### 6️⃣ Start the FastAPI Server
```sh
uvicorn main:app --reload
```

### 7️⃣ Access the Application
- Open your browser and visit: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**
- API Documentation available at: **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

---

## 🛠 Project Structure
```
/your-repo
│── /static          # CSS and JS files
│── /templates       # HTML templates
│── /routes          # API endpoints and web routes
│── /models          # Database models
│── main.py          # FastAPI application entry point
│── config.py        # Configuration settings
│── requirements.txt # Dependencies
│── README.md        # Project documentation
```

---

## 🔗 API Endpoints
| Method | Endpoint              | Description          |
|--------|-----------------------|----------------------|
| GET    | `/students`           | View all students   |
| POST   | `/students/add`       | Add a new student   |
| GET    | `/students/edit/{id}` | Edit student form   |
| POST   | `/students/edit/{id}` | Update student info |
| POST   | `/students/delete/{id}` | Delete a student  |

---

## ❓ Troubleshooting
If you encounter database connection errors:
1. Check if MySQL is running: `sudo service mysql status`
2. Verify database credentials in `config.py`
3. Ensure MySQL driver **PyMySQL** is installed:
   ```sh
   pip install pymysql
   ```
4. Restart the FastAPI server and try again.

---

## 📜 License
This project is open-source and available under the **MIT License**.

---

## 💡 Author
Developed by **Firdavs Qobilov**.

For any issues, feel free to open a GitHub issue or reach out! 🚀

