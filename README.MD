# 🚀 User Management API

![Python](https://img.shields.io/badge/python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-modern-green)
![SQLAlchemy](https://img.shields.io/badge/ORM-SQLAlchemy%202.0-red)
![MySQL](https://img.shields.io/badge/database-MySQL-orange)
![Auth](https://img.shields.io/badge/auth-JWT%20%2B%20OAuth2-yellow)
![Status](https://img.shields.io/badge/status-functional-brightgreen)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

## 📖 Overview

A RESTful API for managing users and tasks with JWT-based authentication, role-based access control (admin/user), and a layered architecture designed for real-world backend applications.

This project was built as a portfolio project to demonstrate backend development skills using FastAPI, focusing on real-world concepts like authentication, database relationships, and API design.

---

## 🌐 Live Demo

- **API Base URL:** https://user-management-api-awkr.onrender.com  
- **Swagger UI:** https://user-management-api-awkr.onrender.com/docs  

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
git clone https://github.com/rafaelemidiolopes/User-Management-API.git  
cd user-management-api
```

### 2. Create virtual environment

```bash
python -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=user_management_api
SECRET_KEY=your-super-secret-key
```

### 5. Run the application

```bash
uvicorn main:app --reload
```

---

## 🔐 Authentication

This API uses JWT tokens with OAuth2 Password Bearer flow.

Get token:

```bash
curl -X POST "http://localhost:8000/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=user@example.com&password=yourpassword"
```

Use token:

```http
Authorization: Bearer <your_token>
```

👉 Full documentation available at: https://user-management-api-awkr.onrender.com/docs

---

## 📌 Main Endpoints

| Access Level | Endpoints |
|-------------|----------|
| Public | POST /login |
| User | GET /me, PATCH /me, DELETE /me |
| Admin | POST /users, GET /users, PATCH /users/{id}, DELETE /users/{id} |

---

## 🧱 Architecture

The project follows a layered structure:

| Layer | Responsibility |
|------|----------------|
| Models | Database structure (SQLAlchemy) |
| Schemas | Validation & serialization (Pydantic) |
| Services | Business logic |
| Security | Authentication & authorization |
| Routers | HTTP layer |

This separation improves:  
Maintainability  
Readability  
Scalability  

---

## 🎯 Purpose

This project demonstrates backend development skills, including authentication, API design, database relationships, and production deployment.

---

## 👨‍💻 Author

Rafael Emídio  

---

## 📄 License

MIT License
