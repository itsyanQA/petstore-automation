from enum import Enum


class OrderStatus(str, Enum):
    placed = "placed"
    approved = "approved"
    delivered = "delivered"
