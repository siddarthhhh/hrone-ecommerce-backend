from pydantic import BaseModel
from typing import List

class ProductSchema(BaseModel):
    name: str
    price: float
    size: str

class ProductOut(ProductSchema):
    id: str
