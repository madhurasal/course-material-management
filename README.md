
# Course Material Management System

A **Course Material Management System** built with **Django** that allows users to manage and access educational course materials efficiently.
This platform helps organize study resources, upload course-related content, and manage learning materials in one place.

---

## Features

* User-friendly dashboard
* Upload and manage course materials
* Organized material categories
* Media file handling
* Responsive templates
* Admin panel for management
* Secure backend with Django

---

## Tech Stack

### Backend:

* Python
* Django

### Frontend:

* HTML
* CSS
* Bootstrap

### Database:

* SQLite

---

## Project Structure

```bash id="8r0pxn"
course-material-management/
│── blog/
│── iblogs/
│── media/
│── templates/
│── db.sqlite3
│── manage.py
│── README.md
```

---

## Installation

### 1. Clone the repository

```bash id="g9msnl"
git clone https://github.com/your-username/course-material-management.git
cd course-material-management
```

### 2. Create virtual environment

```bash id="oj8a8p"
python -m venv env
```

### 3. Activate environment

**Windows**

```bash id="x7x7ms"
env\Scripts\activate
```

**Mac/Linux**

```bash id="h4fq9t"
source env/bin/activate
```

### 4. Install dependencies

```bash id="jw4w0n"
pip install -r requirements.txt
```

### 5. Run migrations

```bash id="dj9bpl"
python manage.py migrate
```

### 6. Start server

```bash id="c4p0e8"
python manage.py runserver
```

Then open:

```bash id="7sq7ca"
http://127.0.0.1:8000/
```

---

## Future Enhancements

* User authentication system
* File download permissions
* Course-wise categorization
* Search functionality
* Notifications for updates

---



GitHub: https://github.com/madhurasal
