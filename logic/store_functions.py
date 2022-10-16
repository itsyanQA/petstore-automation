from datetime import datetime
from random import randint, choice
from models.enum.OrderStatus import OrderStatus
from models.request.Order import Order
from helper import random_functions


def build_order_object(id_: int, petId: int= None, quantity: int = None, shipDate = None, status: OrderStatus = None, complete: bool = None):
    """Builds the nessaccary data for the order object"""
    order_object = Order(id=id_)

    if id_ is not None:
        order_object.id = id_
    else:
        order_object.id = random_functions.get_random_number(1)

    if petId is not None:
        order_object.petId = petId
    else:
        order_object.petId = random_functions.get_random_number(randint(1, 9))

    if quantity is not None:
        order_object.quantity = quantity
    else:
        order_object.quantity = random_functions.get_random_number(randint(1, 9))

    if shipDate is not None:
        order_object.shipDate = shipDate
    else:
        order_object.shipDate = "2022-10-08T00:45:48.513+0000"

    if status is not None:
        order_object.status = status
    else:
        order_object.status = choice(list(OrderStatus))

    if complete is not None:
        order_object.complete = complete
    else:
        order_object.complete = choice([True, False])

    return order_object








