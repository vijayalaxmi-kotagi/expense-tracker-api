from fastapi import FastAPI
from src.models import Expense

app = FastAPI()

from src.storage import load_expenses, save_expenses



@app.get("/")
def home():
    return {
        "message": "Welcome to Smart Expense Tracker API!"
    }


@app.post("/expenses")
def add_expense(expense: Expense):
    expenses = load_expenses()

    expense_dict = expense.model_dump(mode="json")

    expenses.append(expense_dict)

    save_expenses(expenses)

    return {
        "message": "Expense added successfully!",
        "expense": expense
    }

@app.get("/expenses")
def get_expenses():
    return load_expenses()

@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):
    expenses = load_expenses()

    if expense_id < 0 or expense_id >= len(expenses):
        return {"error": "Expense not found"}

    deleted = expenses.pop(expense_id)

    save_expenses(expenses)

    return {
        "message": "Expense deleted successfully!",
        "deleted": deleted
    }

@app.put("/expenses/{expense_id}")
def update_expense(expense_id: int, updated_expense: Expense):
    expenses = load_expenses()

    if expense_id < 0 or expense_id >= len(expenses):
        return {"error": "Expense not found"}

    expenses[expense_id] = updated_expense.model_dump(mode="json")

    save_expenses(expenses)

    return {
        "message": "Expense updated successfully!",
        "expense": updated_expense
    }

@app.get("/expenses/category/{category}")
def get_expenses_by_category(category: str):
    expenses = load_expenses()

    result = []

    for expense in expenses:
        if expense["category"].lower() == category.lower():
            result.append(expense)

    return result

@app.get("/expenses/total")
def get_total_expense():
    expenses = load_expenses()

    total = 0

    for expense in expenses:
        total += expense["amount"]

    return {
        "total_expense": total
    }

@app.get("/expenses/date/{expense_date}")
def get_expenses_by_date(expense_date: str):
    expenses = load_expenses()

    result = []

    for expense in expenses:
        if expense["date"] == expense_date:
            result.append(expense)

    return result

@app.get("/expenses/summary")
def get_summary():
    expenses = load_expenses()

    summary = {}

    for expense in expenses:
        category = expense["category"]

        if category in summary:
            summary[category] += expense["amount"]
        else:
            summary[category] = expense["amount"]

    return summary