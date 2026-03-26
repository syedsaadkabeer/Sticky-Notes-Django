# Django Sticky Notes App

## Project Overview

This is a Django-based Sticky Notes web application developed as a Web Engineering assignment by Syed Saad Kabeer. 
It allows users to register, log in, and manage their personal notes securely.
This project demonstrates Django fundamentals including models, forms, views, authentication, and user-based data protection.

Each user can create, edit, and delete their own notes. Notes are displayed as colored cards.

---

## Features

- User Registration
- User Login & Logout
- Create Notes
- View Notes
- Edit Notes
- Delete Notes
- User-specific data (no access to others' notes)
- Color-based note display

---

## Technologies Used

- Python
- Django
- SQLite (default database)
- HTML (Django Templates)

---

## Project Structure

sticky_notes_assignment/
└── sticky_project/
├── manage.py
├── notes/
│ ├── models.py
│ ├── views.py
│ ├── forms.py
│ ├── urls.py
│ ├── templates/
│ └── admin.py
└── sticky_project/
├── settings.py
├── urls.py


---

## Setup Instructions

### 1. Clone or Download Project

git clone <your-repo-link>
OR download ZIP and extract.

---

### 2. Navigate to Project Folder

cd sticky_project

---

### 3. Create Virtual Environment

python -m venv venv

Activate:

Windows:
venv\Scripts\activate


---

### 4. Install Dependencies

pip install django

---

### 5. Run Migrations

python manage.py makemigrations
python manage.py migrate

---

### 6. Create Superuser (Optional)

python manage.py createsuperuser

---

### 7. Run Server

python manage.py runserver


---

## Usage

- Register a new account
- Login using credentials
- Create notes
- Edit or delete notes
- Each user can only see their own notes

---

## Security Implementation

- Notes are filtered using:
Note.objects.filter(owner=request.user)

- Edit/Delete protected using:
get_object_or_404(Note, pk=pk, owner=request.user)

This ensures users cannot access or modify other users' notes.

---

## Notes

- All code comments are written in Roman Urdu as per assignment requirement.

---

## Author

Syed Saad Kabeer
