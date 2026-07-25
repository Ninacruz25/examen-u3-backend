from fastapi import FastAPI, HTTPException

from app.models import Item, ItemCreate, ItemUpdate
from app.storage import ItemStore

app = FastAPI(title="examen-u3 items API")
store = ItemStore()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/items", response_model=list[Item])
def list_items() -> list[Item]:
    return store.list()


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    item = store.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.post("/items", response_model=Item, status_code=201)
def create_item(payload: ItemCreate) -> Item:
    return store.create(payload)


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, payload: ItemUpdate) -> Item:
    item = store.update(item_id, payload)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int) -> None:
    deleted = store.delete(item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found")
