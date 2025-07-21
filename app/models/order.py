from pydantic import BaseModel
from typing import List

class OrderItemSchema(BaseModel):
    productId: str
    qty: int

class OrderSchema(BaseModel):
    userID: str
    items: List[OrderItemSchema]
