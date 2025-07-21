from pydantic import BaseModel
from typing import List

class SizeItem(BaseModel):
    size: str
    quantity: int

class ProductCreate(BaseModel):
    name: str
    price: float
    sizes: List[SizeItem]

class ProductOut(BaseModel):
    id: str
    name: str
    price: float
