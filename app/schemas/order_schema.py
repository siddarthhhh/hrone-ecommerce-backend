from pydantic import BaseModel
from typing import List

class OrderSchema(BaseModel):
    user_id: str
    products: List[str]

class OrderOut(OrderSchema):
    id: str
