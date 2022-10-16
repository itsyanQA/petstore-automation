from enum import Enum

from pydantic import BaseModel


class Status(str, Enum):
    available = "available"
    pending: str = "pending"
    sold: str = "sold"

