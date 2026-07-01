#  RiskGuard

> A fraud risk monitoring platform built with FastAPI to analyze financial transactions, calculate risk scores, and support manual fraud investigation.

---

## Overview

RiskGuard is a backend application designed to simulate a real-world fraud monitoring platform used by financial institutions and fintech companies.

The system receives transactions, evaluates their risk using predefined business rules, stores the results, and provides a secure dashboard for analysts to review suspicious activity.

This project was built to demonstrate backend engineering concepts such as layered architecture, authentication, business rules, API design, and clean code.

---

## Features

- JWT Authentication
- User Registration & Login
- Transaction Risk Analysis
- Risk Scoring Engine
- Manual Transaction Review
- Protected Dashboard
- High-Risk Transactions
- Pagination
- Global Exception Handling
- Structured Logging
- Environment Configuration (.env)
- Swagger Documentation

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| FastAPI | REST API |
| SQLAlchemy | ORM |
| SQLite | Database |
| Pydantic | Validation |
| JWT | Authentication |
| Passlib | Password Hashing |
| Python | Backend Language |

---

## Project Structure

```text
app/
├── api/
├── core/
├── exceptions/
├── models/
├── repositories/
├── schemas/
├── services/
└── main.py
```

---

## Architecture

```text
Client
      │
      ▼
API (FastAPI)
      │
      ▼
Service Layer
      │
      ▼
Repository Layer
      │
      ▼
SQLite Database
```

---

## Authentication Flow

```text
Register
      │
      ▼
Login
      │
      ▼
JWT Token
      │
      ▼
Protected Endpoints
```

---

## Main Endpoints

### Authentication

```
POST /auth/register
POST /auth/login
GET  /auth/me
```

### Transactions

```
POST   /transactions
GET    /transactions
GET    /transactions/{id}
PATCH  /transactions/{id}/review
```

### Dashboard

```
GET /dashboard/summary
GET /dashboard/high-risk
```

---

## Running the Project

Clone the repository

```bash
git clone https://github.com/brancestack/riskguard.git
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
uvicorn app.main:app --reload
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

## Future Improvements

- Docker support
- PostgreSQL
- Machine Learning risk model
- Email notifications
- React Dashboard
- Role-based authorization

---

## Author

**Brancestack**

Backend Developer focused on backend engineering, financial systems and scalable software.
