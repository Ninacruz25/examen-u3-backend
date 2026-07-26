from fastapi.testclient import TestClient


def auth_headers(api_key: str) -> dict[str, str]:
    return {"x-api-key": api_key}


def test_create_item(client: TestClient, api_key: str) -> None:
    payload = {"nombre": "manzana", "descripcion": "fruta roja"}
    response = client.post("/items", headers=auth_headers(api_key), json=payload)
    assert response.status_code == 201
    body = response.json()
    assert body["id"] == 1
    assert body["nombre"] == "manzana"
    assert body["descripcion"] == "fruta roja"


def test_list_items_returns_all_created(client: TestClient, api_key: str) -> None:
    client.post("/items", headers=auth_headers(api_key), json={"nombre": "a"})
    client.post("/items", headers=auth_headers(api_key), json={"nombre": "b"})

    response = client.get("/items", headers=auth_headers(api_key))

    assert response.status_code == 200
    assert len(response.json()) == 2


def test_get_single_item(client: TestClient, api_key: str) -> None:
    created = client.post("/items", headers=auth_headers(api_key), json={"nombre": "a"}).json()

    response = client.get(f"/items/{created['id']}", headers=auth_headers(api_key))

    assert response.status_code == 200
    assert response.json() == created


def test_get_single_item_not_found(client: TestClient, api_key: str) -> None:
    response = client.get("/items/999", headers=auth_headers(api_key))
    assert response.status_code == 404


def test_update_item(client: TestClient, api_key: str) -> None:
    created = client.post("/items", headers=auth_headers(api_key), json={"nombre": "a"}).json()

    response = client.put(
        f"/items/{created['id']}",
        headers=auth_headers(api_key),
        json={"nombre": "a actualizado", "descripcion": "nueva descripcion"},
    )

    assert response.status_code == 200
    assert response.json()["nombre"] == "a actualizado"


def test_update_item_not_found(client: TestClient, api_key: str) -> None:
    response = client.put("/items/999", headers=auth_headers(api_key), json={"nombre": "x"})
    assert response.status_code == 404


def test_delete_item(client: TestClient, api_key: str) -> None:
    created = client.post("/items", headers=auth_headers(api_key), json={"nombre": "a"}).json()

    response = client.delete(f"/items/{created['id']}", headers=auth_headers(api_key))
    assert response.status_code == 204

    follow_up = client.get(f"/items/{created['id']}", headers=auth_headers(api_key))
    assert follow_up.status_code == 404


def test_delete_item_not_found(client: TestClient, api_key: str) -> None:
    response = client.delete("/items/999", headers=auth_headers(api_key))
    assert response.status_code == 404
