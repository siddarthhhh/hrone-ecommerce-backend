from fastapi import APIRouter, Request
from app.models.product import ProductSchema
from bson import ObjectId

router = APIRouter()

@router.post("/products", status_code=201)
async def create_product(request: Request, product: ProductSchema):
    db = request.app.database
    result = await db.products.insert_one(product.dict())
    return { "id": str(result.inserted_id) }

@router.get("/products")
async def list_products(request: Request, name: str = None, size: str = None, limit: int = 10, offset: int = 0):
    db = request.app.database
    query = {}
    
    if name:
        query["name"] = {"$regex": name, "$options": "i"}
    if size:
        query["sizes.size"] = size

    cursor = db.products.find(query).skip(offset).limit(limit)
    products = await cursor.to_list(length=limit)

    product_list = [
        {
            "id": str(prod["_id"]),
            "name": prod["name"],
            "price": prod["price"]
        }
        for prod in products
    ]

    return {
        "data": product_list,
        "page": {
            "next": str(offset + limit),
            "limit": len(product_list),
            "previous": offset - limit
        }
    }
