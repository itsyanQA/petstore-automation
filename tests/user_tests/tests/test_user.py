import unittest
from typing import Final
import pytest
from helper import random_functions
from models.enum.User import User
from models.request.Login import Login
from models.response.ApiResponse import ApiResponse
from scheme_custom.ApiResponseMetaData import ApiResponseMetaData
from scheme_custom.UserMetaData import UserMetaData
from tests.user_tests.client_wrapper.WrapperUserEndpoints import WrapperUserEndpoints
from logic import user_functions


@pytest.mark.order(3)
class TestUser(WrapperUserEndpoints, unittest.TestCase):
    USERNAME: Final[str] = "UpdatingUserNameTest"

    def tearDown(self):
        """Deletes our final username just in-case someone created it, so the test won't fail."""
        search_username = super().get_user_by_username(self.USERNAME, should_ignore_exception=True)
        if type(search_username) is ApiResponseMetaData:
            pass
        else:
            super().delete_user(self.USERNAME)

    def test_createUser_success(self):
        """Create a user and validate it has been successfully created"""
        # arrange & action
        user_object = self.__create_a_user()

        # assert
        user_details: UserMetaData = super().get_user_by_username(user_object.username)
        self.assertEqual(user_details.user.username, user_object.username)
        self.assertEqual(user_details.user.userStatus, user_object.userStatus)
        self.assertEqual(user_details.user.id, user_object.id)
        self.assertEqual(user_details.user.firstName, user_object.firstName)
        self.assertEqual(user_details.user.lastName, user_object.lastName)
        self.assertEqual(user_details.user.phone, user_object.phone)
        self.assertEqual(user_details.user.email, user_object.email)
        self.assertEqual(user_details.user.password, user_object.password)

    def test_createUser_updateUser_success(self):
        """Create a user, update the username and validate is has been successfully changed, and all the other values
        stayed the same."""

        # arrange
        user_object_original = self.__create_a_user()
        get_details_original_user: UserMetaData = super().get_user_by_username(user_object_original.username)
        user_object_update: User = user_functions.build_user_object(id_=user_object_original.id, username=self.USERNAME, firstName=user_object_original.firstName, lastName=user_object_original.lastName, phone=user_object_original.phone, email=user_object_original.email, userStatus=user_object_original.userStatus, password=user_object_original.password)

        # action
        update_user_details: ApiResponse = super().put_update_user(user_object_original.username, user_object_update)

        # assert
        get_details_updated_user: UserMetaData = super().get_user_by_username(user_object_update.username)

        self.assertEqual(update_user_details.code, 200)
        self.assertNotEqual(get_details_original_user.user.username, get_details_updated_user.user.username)
        self.assertEqual(get_details_updated_user.user.username, self.USERNAME)
        self.assertEqual(get_details_original_user.user.id, get_details_updated_user.user.id)
        self.assertEqual(get_details_original_user.user.userStatus, get_details_updated_user.user.userStatus)
        self.assertEqual(get_details_original_user.user.firstName, get_details_updated_user.user.firstName)
        self.assertEqual(get_details_original_user.user.lastName, get_details_updated_user.user.lastName)
        self.assertEqual(get_details_original_user.user.email, get_details_updated_user.user.email)
        self.assertEqual(get_details_original_user.user.password, get_details_updated_user.user.password)

    # TODO: Add test that deletes a user successfully, and one that deletes a user that doesn't exist

    def test_createUser_deleteUser_success(self):
        """Creates a generic user, deletes it and validate it has been successfully deleted."""
        # arrange
        user_object: User = self.__create_a_user()

        # action
        delete_user: ApiResponse = super().delete_user(user_object.username)

        # assert
        self.assertEqual(delete_user.code, 200)
        self.assertEqual(delete_user.type, "unknown")
        self.assertEqual(delete_user.message, user_object.username)

        deleted_user_details: ApiResponseMetaData = super().get_user_by_username(user_object.username, should_ignore_exception=True)
        self.assertEqual(deleted_user_details.status_code, 404)
        self.assertEqual(deleted_user_details.api_response.code, 1)
        self.assertEqual(deleted_user_details.api_response.type, "error")
        self.assertEqual(deleted_user_details.api_response.message, "User not found")

    def test_createUser_deleteUser_invalid(self):
        """Generate a non existing user, try to delete and expect for a 404 response."""
        # arrange
        generated_username: str = random_functions.get_random_string(50)

        # action
        delete_user: int = super().delete_user(generated_username, should_ignore_exception=True)

        # assert
        self.assertEqual(delete_user, 404)

    def test_login_success(self):
        """Create generic user, send a GET request for login endpoint with query string, assert that we've logged in."""
        # arrange
        user_object: User = self.__create_a_user()

        # action
        login_details: ApiResponse = super().get_user_login(Login(username=user_object.username, password=user_object.password))

        # assert
        login_message_without_session_number: str = " ".join(login_details.message.split(' ')[:3])
        self.assertEqual(login_details.code, 200)
        self.assertEqual(login_details.type, 'unknown')
        self.assertEqual(login_message_without_session_number, "logged in user")

    def test_logout_success(self):
        """Send GET request for logout endpoint, assert for successful results."""
        # action
        logout_details: ApiResponse = super().get_user_logout()

        # assert
        self.assertEqual(logout_details.code, 200)
        self.assertEqual(logout_details.type, 'unknown')
        self.assertEqual(logout_details.message, 'ok')

    def test_createMultipleUsersList_success(self):
        """Create 3 users, and create them all at once with POST request using user/createWithList endpoint"""
        # arrange
        user1: User = user_functions.build_user_object()
        user2: User = user_functions.build_user_object()
        user3: User = user_functions.build_user_object()

        # action
        users_object: list[dict[User]] = [dict(user1), dict(user2), dict(user3)]
        multiple_user_details: ApiResponse = super().post_create_users_with_list(users_object)

        # assert
        self.assertEqual(multiple_user_details.code, 200)
        self.assertEqual(multiple_user_details.type, 'unknown')
        self.assertEqual(multiple_user_details.message, 'ok')

    def test_createMultipleUsersList_invalid(self):
        """Send false object to user/createWithList using POST request, validate status 500 is returned."""
        # arrange
        invalid_object = {}

        # action
        multiple_user_details: ApiResponse = super().post_create_users_with_list(invalid_object, should_ignore_exception=True)

        # assert
        self.assertEqual(multiple_user_details.code, 500)
        self.assertEqual(multiple_user_details.type, 'unknown')
        self.assertEqual(multiple_user_details.message, 'something bad happened')

    # ---------------------------------------------------Class Methods--------------------------------------------------

    def __create_a_user(self, id_: int = None, username: str = None, firstName: str = None, lastName: str = None, email: str = None, password: str = None, phone: str = None, userStatus: int = None):
        """Creates a generic user and sends it via POST request, option to customize the object is possible with the
        params. """
        user_object: User = user_functions.build_user_object(id_, username, firstName, lastName, email, password, phone, userStatus)
        super().post_create_user(user_object)
        return user_object
