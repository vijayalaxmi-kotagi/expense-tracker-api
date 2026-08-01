from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_add_expense():
    response = client.post(
        "/expenses",
        json={
            "title": "Test Expense",
            "amount": 100,
            "category": "testing",
            "date": "2026-07-31"
        }
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Expense added successfully!"


def test_get_expenses():
    response = client.get("/expenses")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_total():
    response = client.get("/expenses/total")
    assert response.status_code == 200
    assert "total_expense" in response.json()


def test_summary():
    response = client.get("/expenses/summary")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)