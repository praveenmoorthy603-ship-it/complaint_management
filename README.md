# Complaint Management System API

A Django REST Framework (DRF) based Complaint Management System that allows users to register, log in using JWT authentication, and manage customer complaints efficiently.

## 🚀 Live Base URL

`https://complaint-management-5hg9.onrender.com/app/`

---

# 📌 Project Overview

The Complaint Management System API is designed to handle complaint registration, tracking, filtering, searching, ordering, pagination, and dashboard analytics.

### Key Features:

* User Signup
* User Login with JWT Token
* Create Complaint
* View All Complaints
* View Complaint by ID
* Update Complaint
* Delete Complaint
* Filter Complaints
* Search Complaints
* Complaint Dashboard Analytics
* Ordering by Date / Priority
* Pagination Support
* Secure API using Token Authentication

---

# 🛠️ Tech Stack

### Backend:

* Python
* Django
* Django REST Framework (DRF)

### Authentication:

* JWT (Simple JWT)

### Database:

* SQLite (default) / PostgreSQL (deployment ready)

### Deployment:

* Render

---

# 📂 Project Structure

```bash
complaint-management/
│── app/
│   ├── models.py
│   ├── views.py
│   ├── serializer.py
│   ├── urls.py
│
│── manage.py
│── requirements.txt
│── README.md
```

---

# 🔐 Authentication APIs

## 1️⃣ Signup

### Endpoint:

```bash
POST /signup/
```

### Request Body:

```json
{
  "username":"praveen",
  "password":"12345"
}
```

### Response:

```json
{
  "Message":"signUp successfully"
}
```

---

## 2️⃣ Login

### Endpoint:

```bash
POST /login/
```

### Request Body:

```json
{
  "username":"praveen",
  "password":"12345"
}
```

### Response:

```json
{
  "Message":"LogIn successfully",
  "Data":{
    "token":{
      "refresh":"your_refresh_token",
      "access":"your_access_token"
    }
  }
}
```

---

# 📝 Complaint APIs

## 3️⃣ Get All Complaints

### Endpoint:

```bash
GET /complaintview/
```

### Authorization:

```bash
Bearer Token Required
```

---

## 4️⃣ Create Complaint

### Endpoint:

```bash
POST /complaintview/
```

### Request Body:

```json
{
  "title":"Network Issue",
  "description":"Internet not working",
  "category":1,
  "status":"Pending",
  "priority":"High",
  "customer_name":"Praveen",
  "email":"praveen@gmail.com",
  "location":"Chennai"
}
```

---

## 5️⃣ Get Complaint by ID

### Endpoint:

```bash
GET /complaintid/<id>/
```

---

## 6️⃣ Update Complaint

### Endpoint:

```bash
PUT /complaintid/<id>/
```

---

## 7️⃣ Delete Complaint

### Endpoint:

```bash
DELETE /complaintid/<id>/
```

---

# 🔍 Filter API

### Endpoint:

```bash
GET /filter/?status=Pending&priority=High&location=Chennai
```

### Available Filters:

* status
* priority
* category *(Note: current code uses `categroy` typo in query param)*
* location

---

# 🔎 Search API

### Endpoint:

```bash
GET /search/?search=network
```

### Search Fields:

* Title
* Description
* Customer Name
* Location

---

# 📊 Dashboard API

### Endpoint:

```bash
GET /dashboard/
```

### Dashboard Data:

* Total Complaints
* Pending Complaints
* Resolved Complaints
* In Progress Complaints
* High Priority
* Medium Priority
* Low Priority

---

# 📅 Ordering API

### Endpoint:

```bash
GET /order/?ordering=-created_at
```

### Options:

### Date:

* `created_at`
* `-created_at`

### Priority:

* `priority`
* `-priority`

---

# 📄 Pagination API

### Endpoint:

```bash
GET /page/?page=2
```

### Features:

* Count
* Next Page
* Previous Page
* Results

---

# 🗃️ Database Models

## Category Model:

```python
name
```

## Complaint Model:

```python
title
description
category
status
priority
customer_name
email
location
created_at
updated_at
```

---

# ⚙️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone <your-repo-link>
cd complaint-management
```

## 2️⃣ Create Virtual Environment

```bash
python -m venv env
```

## 3️⃣ Activate Environment

### Windows:

```bash
env\Scripts\activate
```

### Mac/Linux:

```bash
source env/bin/activate
```

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 5️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## 6️⃣ Run Server

```bash
python manage.py runserver
```

---

# 🌐 Deployment

### Live on Render:

```bash
https://complaint-management-5hg9.onrender.com/app/
```

---

# 📌 Future Improvements

* Role-based authentication (Admin/User)
* Email notifications
* Complaint status tracking
* Swagger API Documentation
* Frontend Integration
* File Upload for Complaint Evidence

---

# 👨‍💻 Author

### Praveen Moorthi

* Python Developer
* Django Backend Developer

---

# ⭐ Conclusion

This project demonstrates strong backend development skills using Django REST Framework, JWT authentication, filtering, searching, pagination, and dashboard analytics—making it suitable for real-world complaint management solutions.


