import json
from json import JSONDecodeError
from typing import Union
from pydantic import ValidationError
from models.request.Pet import Pet
from client.APIRequests import APIRequests
from models.response.ApiResponse import ApiResponse
from scheme_custom.PetMetaData import PetMetaData
from scheme_custom.PetMetaDataCustomStatus import PetMetaDataCustomStatus


class PetEndpoints(APIRequests):

    def get_find_pet_by_status(self, status: str):
        url = f'{super().BASE_URL}/pet/findByStatus?status={status}'
        res = super().http_get(url)
        return res

    def get_find_pet_by_id(self, pet_id: int) -> Union[PetMetaData, PetMetaDataCustomStatus]:
        url = f'{super().BASE_URL}/pet/{pet_id}'
        res = super().http_get(url)
        try:
            return PetMetaData(pet=res.json(), status_code=res.status_code)
        except ValidationError:
            return PetMetaDataCustomStatus(pet=res.json(), status_code=res.status_code)

    def post_add_new_pet(self, body: Union[Pet, dict]):
        url = f'{super().BASE_URL}/pet'
        res = super().http_post(url, json.dumps(dict(body)))
        return res

    def delete_pet_by_id(self, pet_id: int) -> ApiResponse:
        url = f'{super().BASE_URL}/pet/{pet_id}'
        res = super().http_delete(url)
        try:
            return ApiResponse(**res.json())
        except JSONDecodeError:
            return res.status_code

    def put_update_existing_pet(self, body: Pet):
        url = f'{super().BASE_URL}/pet'
        res = super().http_put(url, json.dumps(dict(body)))
        return res

    def post_update_pet_form_data(self, pet_id: int, data: dict, is_form_data: bool):
        url = f'{super().BASE_URL}/pet/{pet_id}'
        res = super().http_post(url, data, is_form_data)
        return ApiResponse(**res.json())

