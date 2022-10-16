from time import sleep
from typing import Union
from models.request.Order import Order
from scheme_custom.ApiResponseMetaData import ApiResponseMetaData
from scheme_custom.StoreMetaData import StoreMetaData
from tests.store_tests.client.StoreEndpoints import StoreEndpoints
from helper import while_conditions


class WrapperStoreEndpoints(StoreEndpoints):
    def post_store_order(self, body: Order):
        return super().post_store_order(body)

    def get_purchase_order_by_id(self, orderId: int, count_to_try: int = 100, is_forced: bool = False, should_ignore_exception: bool = False) -> Union[StoreMetaData, ApiResponseMetaData]:
        if is_forced is False:
            res: Union[StoreMetaData, ApiResponseMetaData] = super().get_purchase_order_by_id(orderId=orderId, should_ignore_exception=should_ignore_exception)
            num_of_call: int = 0

            while num_of_call < count_to_try and not while_conditions.is_order_placed(res):
                num_of_call += 1
                sleep(0.3)
                res: Union[StoreMetaData, ApiResponseMetaData] = super().get_purchase_order_by_id(orderId=orderId, should_ignore_exception=should_ignore_exception)
            else:
                return res
        else:
            return super().get_purchase_order_by_id(orderId=orderId, should_ignore_exception=should_ignore_exception)

    def delete_purchase_order_by_id(self, orderId: int, should_ignore_exception: bool = False):
        return super().delete_purchase_order_by_id(orderId, should_ignore_exception)

    def get_inventory_details(self):
        return super().get_inventory_details()
