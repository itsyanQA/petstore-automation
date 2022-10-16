from pydantic import BaseModel
from models.enum.OrderStatus import OrderStatus


class Order(BaseModel):
    id: int
    petId: int = None
    quantity: int = None
    shipDate: str = None
    status: OrderStatus = None
    complete: bool = None
