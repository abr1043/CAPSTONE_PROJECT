# 📰 CD Blog — Capstone Project

CD Blog is a simple and scalable web application built with **Django** and **Django REST Framework (DRF)**.  
It allows users to manage products and (optionally) blog posts through RESTful APIs — supporting CRUD operations, model relationships, and admin management.

This project is developed as part of the Capstone Project to demonstrate full-stack backend development skills using Django.

---

## 🚀 Features

- 🔧 Django REST Framework–powered API
- 🧩 Model-based database (Product)
- 🗂️ CRUD operations (Create, Read, Update, Delete)
- 🕹️ Django Admin panel for management
- 🕒 Automatic timestamps for records
- 🧱 Scalable structure for future extensions (e.g. posts, comments, users)
- 💾 SQLite3 database (default, can be switched to PostgreSQL)

---

## 🏗️ Project Structure

CAPSTONE_PROJECT/
├── cd_blog/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── capstone_project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── manage.py
├── db.sqlite3
├── requirements.txt
└── README.md

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/capstone_project.git
cd capstone_project
