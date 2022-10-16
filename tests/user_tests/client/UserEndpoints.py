import json
from json import JSONDecodeError
from typing import Union
from pydantic import ValidationError
from client.APIRequests import APIRequests
from models.enum.User import User
from models.request.Login import Login
from models.response.ApiResponse import ApiResponse
from scheme_custom.ApiResponseMetaData import ApiResponseMetaData
from scheme_custom.UserMetaData import UserMetaData


class UserEndpoints(APIRequests):
    def post_create_users_with_list(self, user_object: list[dict[User]], should_ignore_exception: bool = False) -> ApiResponse:
        url: str = f"{super().BASE_URL}/user/createWithList"
        res = super().http_post(url, json.dumps(user_object, indent=1), should_ignore_exception=should_ignore_exception)
        return ApiResponse(**res.json())

    def get_user_by_username(self, username: str, should_ignore_exception: bool = False) -> Union[UserMetaData, ApiResponseMetaData]:
        url: str = f"{super().BASE_URL}/user/{username}"
        res = super().http_get(url=url, should_ignore_exception=should_ignore_exception)
        try:
            return ApiResponseMetaData(api_response=res.json(), status_code=res.status_code)
        except (TypeError, ValidationError):
            return UserMetaData(user=res.json(), status_code=res.status_code)

    def put_update_user(self, username: str, body: User) -> ApiResponse:
        url: str = f"{super().BASE_URL}/user/{username}"
        res = super().http_put(url, json.dumps(dict(body)))
        return ApiResponse(**res.json())

    def delete_user(self, username: str, should_ignore_exception: bool = False) -> Union[ApiResponse, int]:
        url: str = f"{super().BASE_URL}/user/{username}"
        res = super().http_delete(url, should_ignore_exception=should_ignore_exception)
        try:
            return ApiResponse(**res.json())
        except JSONDecodeError:
            return res.status_code

    def get_user_login(self, params: Login) -> ApiResponse:
        url: str = f"{super().BASE_URL}/user/login"
        res = super().http_get(url, params=dict(params))
        return ApiResponse(**res.json())

    def get_user_logout(self):
        url: str = f"{super().BASE_URL}/user/logout"
        res = super().http_get(url)
        return ApiResponse(**res.json())

    def post_create_user(self, user_object: User) -> UserMetaData:
        url: str = f"{super().BASE_URL}/user"
        res = super().http_post(url, json.dumps(dict(user_object)))
        return UserMetaData(user=res.json(), status_code=res.status_code)
