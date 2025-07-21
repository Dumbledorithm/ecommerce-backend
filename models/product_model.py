from database import db
from bson import ObjectId

async def create_product(product: dict):
    res = await db.products.insert_one(product)
    return str(res.inserted_id)

async def get_products(name=None, size=None, limit=10, offset=0):
    query = {}
    if name:
        query["name"] = {"$regex": name, "$options": "i"}
    if size:
        query["sizes.size"] = size

    cursor = db.products.find(query).skip(offset).limit(limit).sort("_id")
    products = []
    async for product in cursor:
        products.append({
            "id": str(product["_id"]),
            "name": product["name"],
            "price": product["price"]
        })

    return products, offset + limit, max(0, offset - limit)
