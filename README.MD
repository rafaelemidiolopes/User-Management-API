# 🚀 User Management API

![Python](https://img.shields.io/badge/python-3.10+-blue) ![FastAPI](https://img.shields.io/badge/FastAPI-modern-green) ![SQLAlchemy](https://img.shields.io/badge/ORM-SQLAlchemy-red) ![Database](https://img.shields.io/badge/database-MySQL-orange) ![Status](https://img.shields.io/badge/status-in%20development-yellow) ![License](https://img.shields.io/badge/license-MIT-lightgrey)

A RESTful API built with **FastAPI** to manage users and their tasks.  

This project follows a clean architecture approach, separating concerns between routes, services, schemas, and database models.

---

## 📌 Features

- Full CRUD for Users
- Full CRUD for Tasks
- User ↔ Task relationship (One-to-Many)
- Filter tasks:
  - With assigned user
  - Without assigned user
- Efficient relational loading with SQLAlchemy (`joinedload`, `selectinload`)
- Data validation using Pydantic
- Proper HTTP status codes and error handling

---

## 🧱 Tech Stack

- Python 3.10+
- FastAPI
- SQLAlchemy 2.0
- Pydantic
- MySQL
- PyMySQL
- python-dotenv

---

## 📂 Project Structure


.
├── models/ # Database models (SQLAlchemy)
├── schemas/ # Data validation (Pydantic)
├── services/ # Business logic
├── routers/ # API routes
├── database.py # Database connection
├── main.py # Application entry point
├── .env # Environment variables
└── .gitignore


---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/user-management-api.git
cd user-management-api

2. Create and activate virtual environment
python -m venv venv
Linux / macOS
source venv/bin/activate
Windows
venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

If you don't have a requirements file:

pip freeze > requirements.txt

4. Configure environment variables

Create a .env file in the root:

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=user_management_api
5. Run the application
uvicorn main:app --reload
🌐 API Access
Base URL: http://127.0.0.1:8000
Swagger Docs: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc

📌 Endpoints

👤 Users
Method	Endpoint	Description
POST	/users	Create user
GET	/users	List users
GET	/users/{user_id}	Get user
PUT	/users/{user_id}	Update user
DELETE	/users/{user_id}	Delete user
GET	/users/users-with-tasks	Users with tasks
GET	/users/{user_id}/tasks	Get user with tasks

✅ Tasks
Method	Endpoint	Description
POST	/tasks	Create task
GET	/tasks	List tasks
GET	/tasks/{task_id}	Get task
PUT	/tasks/{task_id}	Update task
DELETE	/tasks/{task_id}	Delete task
GET	/tasks/tasks-with-user	Tasks with user
GET	/tasks/tasks-without-user	Tasks without user

🧠 Architecture

Models → Database layer (SQLAlchemy)
Schemas → Data validation and serialization (Pydantic)
Services → Business logic
Routers → HTTP layer (FastAPI)

This separation improves scalability, readability, and maintainability.

⚠️ Limitations
No authentication (JWT not implemented)
No pagination
No automated tests
No database migrations (Alembic not configured)

👨‍💻 Author

Rafael Emídio

📄 License

This project is licensed under the MIT License.