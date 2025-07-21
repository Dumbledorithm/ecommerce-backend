from fastapi import APIRouter
from schemas.order import OrderCreate
from models.order_model import create_order, get_orders_by_user
from bson import ObjectId

router = APIRouter()

@router.post("/orders", status_code=201)
async def create_order_route(order: OrderCreate):
    # Convert string productId to ObjectId for MongoDB
    doc = {
        "userId": order.userId,
        "items": [
            {
                "productId": ObjectId(item.productId),
                "quantity": item.quantity
            } for item in order.items
        ]
    }
    order_id = await create_order(doc)
    return {"id": order_id}


@router.get("/orders/{user_id}")
async def list_orders(user_id: str, limit: int = 10, offset: int = 0):
    orders, next_offset, prev_offset = await get_orders_by_user(user_id, limit, offset)
    return {
        "data": orders,
        "page": {
            "next": next_offset,
            "limit": limit,
            "previous": prev_offset
        }
    }
