📰 Community Discussion Blog API

Developer: Abraham Ojo
Framework: Django Rest Framework (DRF)
Deployment: Live API on Render

Repository: GitHub - CAPSTONE_PROJECT

📖 Project Overview

The Community Discussion Blog API is a RESTful web service built with Django Rest Framework that allows users to create posts, comment, like/unlike, and engage in discussions.
It provides JWT authentication for secure user access and supports pagination, filtering, and searching for efficient data retrieval.

This project serves as the backend of a social platform where people can share ideas, interact with posts, and participate in community discussions.

🚀 Key Features

✅ User Authentication & Authorization

Register, login, and logout using JWT (JSON Web Token).

Secure endpoints — only authenticated users can create or interact with posts.

✅ Post Management

Create, update, delete, and view blog posts.

Supports image uploads and timestamps.

✅ Comment System

Add comments to posts.

Nested comments for better discussions.

✅ Like / Unlike Functionality

Users can like or unlike posts.

✅ Filtering, Searching & Pagination

Search posts by title or author.

Filter posts by date or popularity.

Pagination included for scalable responses.

✅ Comprehensive API Testing

Unit tests ensure endpoint reliability and performance.

🛠️ Tech Stack
Category	Tools / Libraries
Backend Framework	Django, Django REST Framework
Authentication	SimpleJWT
Database	SQLite (development), PostgreSQL (production)
Deployment	Render
Version Control	Git & GitHub
Testing	Django TestCase & DRF test client
⚙️ Installation & Setup

Follow these steps to run the project locally 👇

1️⃣ Clone the repository
git clone https://github.com/abr1043/CAPSTONE_PROJECT.git
cd CAPSTONE_PROJECT

2️⃣ Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate      # For Windows

source venv/bin/activate   # For Mac/Linux

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Create a superuser
python manage.py createsuperuser

6️⃣ Start the server
python manage.py runserver

MY API will be live at:
👉 http://127.0.0.1:8000/

🔑 API Endpoints
Endpoint	Method	Description	Auth
/api/token/	POST	Obtain JWT token	
/api/token/refresh/	POST	Refresh access token	
/api/posts/	GET / POST	List or create posts	✅
/api/posts/<id>/	GET / PUT / DELETE	Retrieve, update, or delete post	✅
/api/comments/	GET / POST	Manage comments	✅
/api/likes/	POST / DELETE	Like or unlike a post	✅
🧪 Running Tests

Run all automated tests to ensure everything works perfectly:

python manage.py test

🌍 Deployment

The project is deployed using Render for continuous integration and hosting.
Environment variables such as SECRET_KEY, DEBUG, and DATABASE_URL are securely stored in Render’s dashboard.

💡 Future Improvements

Add user profile pictures and bios.

Implement notification system for likes/comments.

Add frontend interface (React or Next.js).

Improve admin dashboard analytics.

📬 Contact

Author: Abraham Ojo
📧 [abrahamojo79@gmail.com]
