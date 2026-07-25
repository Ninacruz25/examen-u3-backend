from pydantic import BaseModel


class ItemBase(BaseModel):
    nombre: str
    descripcion: str | None = None


class ItemCreate(ItemBase):
    pass


class ItemUpdate(ItemBase):
    pass


class Item(ItemBase):
    id: int
