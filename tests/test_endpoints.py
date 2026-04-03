from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_suma_endpoint() -> None:
    response = client.post("/suma", json={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"resultado": 5}


def test_resta_endpoint() -> None:
    response = client.post("/resta", json={"a": 5, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"resultado": 2}


def test_multiplicacion_endpoint() -> None:
    response = client.post("/multiplicacion", json={"a": 2, "b": 4})
    assert response.status_code == 200
    assert response.json() == {"resultado": 8}