from fastapi import APIRouter, Request
from app.models.order import OrderSchema
from bson import ObjectId

router = APIRouter()

@router.post("/orders", status_code=201)
async def create_order(request: Request, order: OrderSchema):
    db = request.app.database
    result = await db.orders.insert_one(order.dict())
    return { "id": str(result.inserted_id) }

@router.get("/orders/{user_id}")
async def get_orders(request: Request, user_id: str, limit: int = 10, offset: int = 0):
    db = request.app.database
    query = { "userID": user_id }

    cursor = db.orders.find(query).skip(offset).limit(limit)
    orders = await cursor.to_list(length=limit)

    formatted_orders = []

    for order in orders:
        formatted_items = []
        total_price = 0

        for item in order["items"]:
            product = await db.products.find_one({ "_id": ObjectId(item["productId"]) })
            if not product:
                continue

            formatted_items.append({
                "productDetails": {
                    "id": str(product["_id"]),
                    "name": product["name"]
                },
                "qty": item["qty"]
            })

            total_price += product["price"] * item["qty"]

        formatted_orders.append({
            "id": str(order["_id"]),
            "items": formatted_items,
            "total": total_price
        })

    return {
        "data": formatted_orders,
        "page": {
            "next": str(offset + limit),
            "limit": limit,
            "previous": offset - limit
        }
    }
