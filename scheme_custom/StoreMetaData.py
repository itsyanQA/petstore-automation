from pydantic import BaseModel

from models.request.Order import Order


class StoreMetaData(BaseModel):
    order: Order
    status_code: int
