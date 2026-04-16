from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Calculator API is running"}


def test_sum_endpoint():
    response = client.post("/sum", json={"a": 5, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 8}


def test_subtract_endpoint():
    response = client.post("/subtract", json={"a": 10, "b": 4})
    assert response.status_code == 200
    assert response.json() == {"result": 6}


def test_multiply_endpoint():
    response = client.post("/multiply", json={"a": 6, "b": 7})
    assert response.status_code == 200
    assert response.json() == {"result": 42}