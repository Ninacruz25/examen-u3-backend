from fastapi import APIRouter, Depends, HTTPException

from app.auth import require_api_key
from app.models import Item, ItemCreate, ItemUpdate
from app.storage import ItemStore

router = APIRouter(prefix="/items", tags=["items"], dependencies=[Depends(require_api_key)])
store = ItemStore()


@router.get("", response_model=list[Item])
def list_items() -> list[Item]:
    return store.list()


@router.get("/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    item = store.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.post("", response_model=Item, status_code=201)
def create_item(payload: ItemCreate) -> Item:
    return store.create(payload)


@router.put("/{item_id}", response_model=Item)
def update_item(item_id: int, payload: ItemUpdate) -> Item:
    item = store.update(item_id, payload)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.delete("/{item_id}", status_code=204)
def delete_item(item_id: int) -> None:
    deleted = store.delete(item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found")
