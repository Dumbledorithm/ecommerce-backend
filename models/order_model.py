from database import db

async def create_order(order: dict):
    res = await db.orders.insert_one(order)
    return str(res.inserted_id)


async def get_orders_by_user(user_id: str, limit: int, offset: int):
    pipeline = [
        {"$match": {"userId": user_id}},
        {"$sort": {"_id": 1}},
        {"$skip": offset},
        {"$limit": limit},
        {
            "$project": {
                "userId": 1,
                "items": 1
            }
        },
        {
            "$unwind": "$items"
        },
        {
            "$lookup": {
                "from": "products",
                "localField": "items.productId",
                "foreignField": "_id",
                "as": "productDetails"
            }
        },
        {"$unwind": "$productDetails"},
        {
            "$addFields": {
                "items.productDetails": {
                    "name": "$productDetails.name",
                    "id": {"$toString": "$productDetails._id"}
                },
                "items.qty": "$items.quantity",
                "itemTotal": {"$multiply": ["$productDetails.price", "$items.quantity"]}
            }
        },
        {
            "$group": {
                "_id": "$_id",
                "items": {
                    "$push": {
                        "productDetails": "$items.productDetails",
                        "qty": "$items.qty"
                    }
                },
                "total": {"$sum": "$itemTotal"}
            }
        },
        {
            "$project": {
                "_id": 0,
                "id": {"$toString": "$_id"},
                "items": 1,
                "total": 1
            }
        }
    ]

    orders = []
    async for doc in db.orders.aggregate(pipeline):
        orders.append(doc)

    return orders, offset + limit, max(0, offset - limit)
