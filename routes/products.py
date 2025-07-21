from fastapi import APIRouter
from schemas.product import ProductCreate
from models.product_model import create_product, get_products
from typing import Optional

router = APIRouter()

@router.post("/products", status_code=201)
async def create_product_route(product: ProductCreate):
    id = await create_product(product.dict())
    return {"id": id}

@router.get("/products")
async def list_products(
    name: Optional[str] = None,
    size: Optional[str] = None,
    limit: int = 10,
    offset: int = 0
):
    products, next_offset, prev_offset = await get_products(name, size, limit, offset)
    return {
        "data": products,
        "page": {
            "next": next_offset,
            "limit": limit,
            "previous": prev_offset
        }
    }
