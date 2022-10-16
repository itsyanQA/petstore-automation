import json
from typing import Union
from client.APIRequests import APIRequests
from models.request.Order import Order
from models.response.ApiResponse import ApiResponse
from scheme_custom.ApiResponseMetaData import ApiResponseMetaData
from scheme_custom.StoreMetaData import StoreMetaData


class StoreEndpoints(APIRequests):
    def post_store_order(self, body: Order):
        url: str = f'{super().BASE_URL}/store/order'
        res = super().http_post(url, json.dumps(dict(body)))
        return res

    def get_purchase_order_by_id(self, orderId: int, should_ignore_exception: bool = False) -> Union[StoreMetaData, ApiResponseMetaData]:
        url: str = f'{super().BASE_URL}/store/order/{orderId}'
        res = super().http_get(url=url, should_ignore_exception=should_ignore_exception)
        try:
            return StoreMetaData(order=res.json(), status_code=res.status_code)
        except Exception as e:
            return ApiResponseMetaData(api_response=res.json(), status_code=res.status_code)

    def delete_purchase_order_by_id(self, orderId: int):
        url: str = f'{super().BASE_URL}/store/order/{orderId}'
        res = super().http_delete(url)
        return ApiResponse(**res.json())

    def get_inventory_details(self):
        url: str = f'{super().BASE_URL}/store/inventory'
        res = super().http_get(url)
        return res
