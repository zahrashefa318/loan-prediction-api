<h1 align="center">
  Loan Affordability Prediction API
</h1>

<h3 align="center">
  FastAPI + Machine Learning + JWT Authentication + Idempotency Protection
</h3>

<p align="center">
  A production-style machine learning API for predicting loan affordability using a custom-trained regression model.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue">
  <img src="https://img.shields.io/badge/FastAPI-Backend-success">
  <img src="https://img.shields.io/badge/React-Frontend-blue">
  <img src="https://img.shields.io/badge/SQLAlchemy-ORM-red">
  <img src="https://img.shields.io/badge/Pytest-Testing-yellow">
  <img src="https://img.shields.io/badge/CI/CD-GitHub_Actions-black">
</p>

---

# Features

- Loan affordability prediction using a trained ML model
- FastAPI REST API
- JWT authentication & authorization
- Idempotency-Key protection
- Request payload hashing
- Cached responses for repeated requests
- SQLite + SQLAlchemy persistence
- Background cleanup for expired idempotency keys
- Automated testing with Pytest
- CI/CD pipeline
- React + Bootstrap frontend ready
- Production-style backend architecture

---

# Tech Stack

## Backend

- Python
- FastAPI
- SQLAlchemy
- SQLite
- NumPy
- PyJWT
- Pydantic
- Pytest

## Frontend

- React
- Bootstrap

---

# Project Structure

```bash
project/
│
├── app/
│   └── main.py
│
├── routes/
│   └── predict.py
│
├── services/
│   ├── authorization_check.py
│   ├── hash_request.py
│   ├── idem_check.py
│   ├── return_cached_data.py
│   └── expired_keys_deletion.py
│
├── model/
│   ├── model_loader.py
│   └── model.pkl
│
├── db/
    ├── db_init.py
│   ├── schema.py
│   └── idempo_tbl.py
│
├── test/
│   ├── integration_test/
│   └── unit_test/
│
├── requirements.txt
└── README.md
```

---

# Machine Learning Model

The API uses a custom-trained linear regression model for loan affordability prediction.

## Features Used

- Income
- Savings
- Expenses
- Family Size
- Years Employed
- Age
- Rent
- Debt

## Prediction Flow

1. Input validation using Pydantic
2. Feature normalization
3. Linear regression prediction
4. Denormalization of prediction
5. Negative prediction protection

```python
y_pred = np.maximum(0, y_pred)
```

---

# Authentication

The API uses JWT Bearer Authentication.

Example Authorization Header:

```http
Authorization: Bearer YOUR_JWT_TOKEN
```

---

# Idempotency Protection

The API supports safe repeated POST requests using:

```http
Idempotency-Key
```

Behavior:

- Same key + same payload → cached response returned
- Same key + different payload → `409 Conflict`

Example:

```http
Idempotency-Key: unique_request_key
```

---

# API Endpoint

## POST `/predict`

### Headers

```http
Authorization: Bearer <token>
Idempotency-Key: unique_key
```

### Request Body

```json
{
  "income": 5000,
  "savings": 2000,
  "expenses": 1500,
  "family_size": 3,
  "years_employed": 5,
  "age": 30,
  "rent": 800,
  "debt": 1000
}
```

### Success Response

```json
{
  "predicted loan": 25000.75
}
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/zahrashefa318/loan-prediction-api.git
cd loan-prediction-api
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run API

```bash
uvicorn app.main:app --reload
```

API available at:

```bash
https://loan-prediction-api-pdr2.onrender.com
```

Swagger Documentation:

```bash
https://loan-prediction-api-pdr2.onrender.com/docs
```

---

# Running Tests

Run all tests:

```bash
pytest
```

Run tests with logs:

```bash
pytest -s
```

---

# Example Test Coverage

- JWT authentication tests
- Expired token tests
- Idempotency key existence tests
- Same request caching tests
- Same key + different payload conflict tests
- Model mathematical validation tests
- Expired key deletion tests

---

# Frontend

The API integrates with a React + Bootstrap frontend containing:

- Input fields for all features
- Predict button
- Prediction result display

---

# Future Improvements

- PostgreSQL integration
- Docker containerization
- Redis caching
- Advanced ML models
- Rate limiting
- Cloud deployment
- User management system

---

# Author

## Zahra Shefa

Backend / ML API Engineer focused on:

- FastAPI
- AI-integrated APIs
- ML model deployment
- Production-style backend systems
- Secure API architecture