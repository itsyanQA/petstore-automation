from typing import Union

from models.enum.User import User
from models.request.Login import Login
from models.response.ApiResponse import ApiResponse
from scheme_custom.ApiResponseMetaData import ApiResponseMetaData
from scheme_custom.UserMetaData import UserMetaData
from tests.user_tests.client.UserEndpoints import UserEndpoints


class WrapperUserEndpoints(UserEndpoints):
    def post_create_users_with_list(self, user_object: list[dict[User]], should_ignore_exception: bool = False) -> ApiResponse:
        return super().post_create_users_with_list(user_object, should_ignore_exception)

    def get_user_by_username(self, username: str, should_ignore_exception: bool = False) -> Union[UserMetaData, ApiResponseMetaData]:
        return super().get_user_by_username(username, should_ignore_exception)

    def put_update_user(self, username: str, body: User) -> ApiResponse:
        return super().put_update_user(username, body)

    def delete_user(self, username: str, should_ignore_exception: bool = False) -> Union[ApiResponse, int]:
        return super().delete_user(username, should_ignore_exception=should_ignore_exception)

    def get_user_login(self, params: Login) -> ApiResponse:
        return super().get_user_login(params)

    def get_user_logout(self) -> ApiResponse:
        return super().get_user_logout()

    def post_create_user(self, user_object: User) -> UserMetaData:
        return super().post_create_user(user_object)

