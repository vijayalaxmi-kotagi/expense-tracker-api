# Smart Expense Tracker API

A RESTful API built using FastAPI to manage personal expenses.

## Features

- Add a new expense
- View all expenses
- Update an existing expense
- Delete an expense
- Filter expenses by category
- Filter expenses by date
- Calculate total expenses
- View expense summary by category
- JSON file-based storage
- Interactive Swagger API documentation

## Project Structure

```
ExpenseTracker/
│
├── src/
│   ├── main.py
│   ├── models.py
│   ├── storage.py
│   └── expenses.json
│
├── tests/
├── README.md
├── AI_NOTES.md
└── requirements.txt
```

## Installation

Create a virtual environment

```bash
python -m venv venv
```

Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install fastapi uvicorn pydantic
```

## Run the Server

```bash
uvicorn src.main:app --reload
```

Server URL

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

## Running Tests

```bash
pytest
```

## Technologies Used

- Python
- FastAPI
- Pydantic
- Uvicorn
- JSON
