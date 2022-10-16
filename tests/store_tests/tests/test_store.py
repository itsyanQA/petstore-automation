import unittest
import pytest
from random import randint
from typing import Union, Final

from helper import random_functions
from models.enum.Status import Status
from models.request.Order import Order
from models.response.ApiResponse import ApiResponse
from scheme_custom.ApiResponseMetaData import ApiResponseMetaData
from scheme_custom.StoreMetaData import StoreMetaData
from tests.pet_tests.client.PetEndpoints import PetEndpoints
from logic import store_functions
from tests.store_tests.client_wrapper.WrapperStoreEndpoints import WrapperStoreEndpoints


@pytest.mark.order(2)
class TestStore(WrapperStoreEndpoints, PetEndpoints, unittest.TestCase):
    def test_placeOrder_success(self):
        """Place an order and assert the response info is correct in GET request"""
        # arrange
        order_id: int = randint(1, 9)

        # action
        order = self.__add_generic_order(order_id)

        # assert
        get_purchase_details: Union[StoreMetaData, ApiResponseMetaData] = super().get_purchase_order_by_id(order.id)
        self.assertEqual(get_purchase_details.order.petId, order.petId)
        self.assertEqual(get_purchase_details.order.id, order_id)
        self.assertEqual(get_purchase_details.order.status, order.status)
        self.assertEqual(get_purchase_details.order.complete, order.complete)
        self.assertEqual(get_purchase_details.order.quantity, order.quantity)

    def test_addOrder_deleteOrder_success(self):
        """Add Order with specific id, delete it and assert it has been deleted in DELETE and GET response"""
        # arrange
        order_id: Final[int] = 1
        self.__add_generic_order(order_id)

        # action
        delete_order: ApiResponse = super().delete_purchase_order_by_id(1)

        # assert
        get_order: ApiResponseMetaData = super().get_purchase_order_by_id(orderId=order_id, is_forced=True, should_ignore_exception=True)
        self.assertEqual(delete_order.code, 200)
        self.assertEqual(delete_order.type, "unknown")
        self.assertEqual(delete_order.message, '1')
        self.assertNotEqual(delete_order.code, 404)
        self.assertNotEqual(delete_order.message, "order not found")

        self.assertEqual(get_order.api_response.code, 1)
        self.assertEqual(get_order.api_response.type, "error")
        self.assertEqual(get_order.api_response.message, "Order not found")

    def test_addOrder_deleteOrder_invalid(self):
        """Try to delete an non-existing order, assert that the request returns status 404"""
        # arrange
        order_id: int = random_functions.get_random_number(15)

        # action
        delete_order: ApiResponse = super().delete_purchase_order_by_id(order_id, should_ignore_exception=True)

        # assert
        self.assertEqual(delete_order.code, 404)
        self.assertEqual(delete_order.type, 'unknown')
        self.assertEqual(delete_order.message, 'Order Not Found')

    def test_store_inventory(self):
        """Send a GET request to get all inventory details, assert the existing statuses exist."""
        # action
        inventory_details = super().get_inventory_details()

        # assert
        self.assertEqual(inventory_details.status_code, 200)
        self.assertIsNotNone(inventory_details.json())
        self.assertIn(Status.available, inventory_details.json())
        self.assertIn(Status.pending, inventory_details.json())
        self.assertIn(Status.sold, inventory_details.json())

    # ---------------------------------------------------Class Methods--------------------------------------------------

    def __add_generic_order(self, order_id):
        """Builds a order object and sends it via POST request and returns the object"""
        order_object: Order = store_functions.build_order_object(order_id)
        super().post_store_order(order_object)
        return order_object



