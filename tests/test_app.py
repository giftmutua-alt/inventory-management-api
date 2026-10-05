import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_get_inventory(client):
    response = client.get("/inventory")

    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_get_single_item(client):
    response = client.get("/inventory/1")

    assert response.status_code == 200
    assert response.json["id"] == 1


def test_get_missing_item(client):
    response = client.get("/inventory/999")

    assert response.status_code == 404


def test_create_item(client):
    response = client.post(
        "/inventory",
        json={
            "name": "Test Product",
            "brand": "Test Brand",
            "price": 100,
            "stock": 5
        }
    )

    assert response.status_code == 201
    assert response.json["name"] == "Test Product"


def test_update_item(client):
    response = client.patch(
        "/inventory/1",
        json={
            "price": 999,
            "stock": 50
        }
    )

    assert response.status_code == 200
    assert response.json["price"] == 999


def test_delete_item(client):
    response = client.delete("/inventory/2")

    assert response.status_code == 200