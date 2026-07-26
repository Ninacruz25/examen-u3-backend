from fastapi.testclient import TestClient


def test_items_rejects_request_without_api_key(client: TestClient) -> None:
    response = client.get("/items")
    assert response.status_code == 401


def test_items_rejects_request_with_wrong_api_key(client: TestClient) -> None:
    response = client.get("/items", headers={"x-api-key": "wrong-key"})
    assert response.status_code == 401


def test_create_rejects_request_without_api_key(client: TestClient) -> None:
    response = client.post("/items", json={"nombre": "no deberia crearse"})
    assert response.status_code == 401
    assert client.get("/items", headers={"x-api-key": "test-api-key"}).json() == []
