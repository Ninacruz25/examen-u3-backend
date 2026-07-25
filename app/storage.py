from itertools import count

from app.models import Item, ItemCreate, ItemUpdate


class ItemStore:
    """In-memory storage for items. Data lives only for the lifetime of the process."""

    def __init__(self) -> None:
        self._items: dict[int, Item] = {}
        self._ids = count(1)

    def list(self) -> list[Item]:
        return list(self._items.values())

    def get(self, item_id: int) -> Item | None:
        return self._items.get(item_id)

    def create(self, payload: ItemCreate) -> Item:
        item_id = next(self._ids)
        item = Item(id=item_id, **payload.model_dump())
        self._items[item_id] = item
        return item

    def update(self, item_id: int, payload: ItemUpdate) -> Item | None:
        if item_id not in self._items:
            return None
        item = Item(id=item_id, **payload.model_dump())
        self._items[item_id] = item
        return item

    def delete(self, item_id: int) -> bool:
        return self._items.pop(item_id, None) is not None
