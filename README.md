# Movie Ticket Booking System

A backend system built using **Django** and **Django REST Framework** for managing movie ticket bookings.  
This project includes user authentication with JWT, movie and show management, seat booking, and API documentation using Swagger.

---

## **Tech Stack**
- **Python 3.x**
- **Django 4.x**
- **Django REST Framework**
- **JWT Authentication** (djangorestframework-simplejwt)
- **Swagger Documentation** (drf-yasg)
- **SQLite** (default database)

---

## **Features**
1. **Authentication**
   - User signup and login
   - JWT-based authentication
   - Booking APIs require a valid JWT token

2. **Movies and Shows**
   - Manage movies and their shows
   - Show details include screen, date/time, and total seats

3. **Booking System**
   - Book a specific seat for a show
   - Cancel bookings
   - View all bookings of the logged-in user
   - Business rules enforced: no double booking, no overbooking, canceling frees up seat

4. **API Documentation**
   - Swagger docs available at `/swagger/`
   - Shows all endpoints with request/response schemas
   - JWT authentication integration documented

---

## **Setup Instructions**

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd movie_booking
Create a virtual environment and activate

bash
Copy code
python -m venv venv

# Linux/Mac
source venv/bin/activate

# Windows
venv\Scripts\activate
Install dependencies

bash
Copy code
pip install -r requirements.txt
Apply migrations

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Create a superuser (optional for admin)

bash
Copy code
python manage.py createsuperuser
Run the server

bash
Copy code
python manage.py runserver
Access Swagger API docs

arduino
Copy code
http://127.0.0.1:8000/swagger/
JWT Authentication
Signup

http
Copy code
POST /signup/
Content-Type: application/json

{
  "username": "yourusername",
  "password": "yourpassword"
}
Login

http
Copy code
POST /login/
Content-Type: application/json

{
  "username": "yourusername",
  "password": "yourpassword"
}
Response

json
Copy code
{
  "refresh": "<refresh_token>",
  "access": "<access_token>"
}
Include the access token for booking APIs

makefile
Copy code
Authorization: Bearer <access_token>
