# Task Manager API

A lightweight, high-performance RESTful API for managing tasks, built with **Python**, **FastAPI**, and **Pydantic**.

## 🚀 Features

- **Create Tasks:** Add new tasks with title, description, and completion status.
- **Read Tasks:** Retrieve a list of all tasks or fetch details of a specific task by ID.
- **Update Tasks:** Modify task attributes or mark them as completed.
- **Delete Tasks:** Remove tasks by ID with appropriate HTTP error handling.
- **Interactive Documentation:** Automatically generated Swagger UI for API testing.
- **Data Validation:** Strict request and response schemas using Pydantic models.

## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **Framework:** FastAPI
- **Server:** Uvicorn (ASGI)
- **Data Validation:** Pydantic

## 💻 Getting Started

### Prerequisites

- Python 3.10 or higher
- Git

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/matiassvillalba/task-manager-api.git
   cd task-manager-api
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/Scripts/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install fastapi uvicorn
   ```

### Running the Application

Start the local development server:

```bash
uvicorn main:app --reload
```

The server will start at `http://127.0.0.1:8000`.

## 📚 API Documentation

FastAPI provides automatic interactive documentation. Once the app is running, visit:

- **Swagger UI:** `http://127.0.0.1:8000/docs`
- **ReDoc:** `http://127.0.0.1:8000/redoc`

### Endpoints Summary

| Method | Endpoint | Description | Response Code |
| :--- | :--- | :--- | :--- |
| `GET` | `/` | Health check endpoint | `200 OK` |
| `POST` | `/tasks` | Create a new task | `201 Created` |
| `GET` | `/tasks` | Retrieve all tasks | `200 OK` |
| `GET` | `/tasks/{task_id}` | Retrieve a specific task by ID | `200 OK` / `404 Not Found` |
| `PUT` | `/tasks/{task_id}` | Update an existing task | `200 OK` / `404 Not Found` |
| `DELETE` | `/tasks/{task_id}` | Delete a task by ID | `200 OK` / `404 Not Found` |