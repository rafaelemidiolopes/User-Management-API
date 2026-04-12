# 🚀 User Management API

![Python](https://img.shields.io/badge/python-3.10+-blue )
![FastAPI](https://img.shields.io/badge/FastAPI-modern-green )
![SQLAlchemy](https://img.shields.io/badge/ORM-SQLAlchemy%202.0-red )
![MySQL](https://img.shields.io/badge/database-MySQL-orange )
![Auth](https://img.shields.io/badge/auth-JWT%20%2B%20OAuth2-yellow )
![Status](https://img.shields.io/badge/status-functional-brightgreen )
![License](https://img.shields.io/badge/license-MIT-lightgrey )

---

## 📖 Overview

A RESTful API for managing users and tasks with authentication, authorization, and role-based access control.

This project was built as a portfolio project to demonstrate backend development skills using FastAPI, focusing on real-world concepts like authentication, database relationships, and API design.

---

## 🌐 Live Demo

- Swagger UI:  
👉 https://user-management-api-dco3.onrender.com/docs

---

## 📌 Features

- JWT Authentication with OAuth2 Password Bearer
- Role-based Access Control (Admin vs User)
- User Management:
  - Create users (admin only)
  - Update profile (own user)
  - Change password with validation
  - Promote users to admin
- Task Management (admin only)
- One-to-Many relationship (User → Tasks)
- Data validation with Pydantic v2
- Proper HTTP status codes and error handling
- Environment-based configuration

---

## 🧱 Tech Stack

- Python 3.10+
- FastAPI
- SQLAlchemy 2.0
- Pydantic v2
- PyJWT
- pwdlib (password hashing)
- MySQL
- PyMySQL
- python-dotenv

---

## 📂 Project Structure
```

.
├── models/                 # Database models (SQLAlchemy)
│   ├── users.py
│   └── tasks.py
├── schemas/                # Data validation (Pydantic)
│   ├── users.py
│   └── tasks.py
├── services/               # Business logic
│   ├── users.py
│   ├── tasks.py
│   └── security.py         # Auth & password handling
├── routers/                # API routes
│   ├── users.py
│   └── tasks.py
├── database.py             # Database connection & session
├── main.py                 # Application entry point
├── .env
└── .gitignore

```

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/user-management-api.git
cd user-management-api

2. Create virtual environment
bash
Copy
python -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate

3. Install dependencies
bash
Copy
pip install -r requirements.txt

4. Configure environment variables
Create a .env file:
env
Copy
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=user_management_api
SECRET_KEY=your-super-secret-key

5. Run the application
bash
Copy
uvicorn main:app --reload

🔐 Authentication
This API uses JWT tokens with OAuth2 Password Bearer flow.
Get token
bash
Copy
POST /login
Body:
plain
Copy
username=user@example.com
password=yourpassword
Use token
plain
Copy
Authorization: Bearer <your_token>

👉 Full documentation available at:
https://user-management-api-dco3.onrender.com/docs

📌 Main Endpoints
Public
POST /login
Authenticated (User)
GET /me
PATCH /me
PATCH /me/change-password
DELETE /me

Admin Only
POST /users
GET /users
PATCH /users/{id}
DELETE /users/{id}
PATCH /users/{id}/promote
POST /tasks
GET /tasks
PATCH /tasks/{id}
DELETE /tasks/{id}

🧠 Architecture
The project follows a layered structure:
Models → database structure
Schemas → validation & serialization
Services → business logic
Security → authentication & authorization
Routers → HTTP layer
This separation improves:
maintainability
readability
scalability

🎯 Purpose
This project was built to practice and demonstrate:
Authentication & Authorization (JWT)
API design
Database relationships
Backend architecture
Real-world deployment

⚠️ Limitations
No pagination on list endpoints
No automated tests
No database migrations
No rate limiting

👨‍💻 Author
Rafael Emídio

📄 License
MIT License