from pydantic import BaseModel
from typing import List

class SizeSchema(BaseModel):
    size: str
    quantity: int

class ProductSchema(BaseModel):
    name: str
    price: float
    sizes: List[SizeSchema]
