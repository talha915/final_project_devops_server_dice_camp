from fastapi.testclient import TestClient
from app.index import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI"}

def test_create_item():
    item_data = {"id": 1, "name": "Test Item", "description": "Test Description", "price": 10.0, "tax": 1.5}
    response = client.post("/items/", json=item_data)
    assert response.status_code == 200
    assert response.json() == item_data

def test_search_item_found():
    item_data = {"id": 1, "name": "Test Item", "description": "Test Description", "price": 10.0, "tax": 1.5}
    # client.post("/items/", json=item_data)

    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"result": [item_data]}

def test_search_item_not_found():
    response = client.get("/items/2")
    assert response.status_code == 200
    assert response.json() == {"result": "Not found"}