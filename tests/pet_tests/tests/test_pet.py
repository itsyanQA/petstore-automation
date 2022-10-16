from typing import Final

from helper import random_functions
from logic import pet_functions as helper
from models.enum.Status import Status
from models.request.Pet import Pet
import pytest
import unittest

from models.response.ApiResponse import ApiResponse
from scheme_custom.PetMetaData import PetMetaData
from scheme_custom.PetMetaDataCustomStatus import PetMetaDataCustomStatus
from tests.pet_tests.client.PetEndpoints import PetEndpoints


@pytest.mark.order(1)
class TestPet(PetEndpoints, unittest.TestCase):
    def test_find_pet_by_id_success(self):
        """Create a pet using POST request, find it using GET request and assert the values match"""
        # arrange
        pet_info = self.__create_a_pet()

        # action
        res: PetMetaData = self.get_find_pet_by_id(pet_info['id'])

        # assert
        self.assertEqual(200, res.status_code)
        self.assertEqual(pet_info["name"], res.pet.name)
        self.assertEqual(pet_info["id"], res.pet.id)
        self.assertEqual(pet_info["photoUrls"], res.pet.photoUrls)
        self.assertEqual(pet_info["status"], res.pet.status)

    def test_find_pet_by_available_status_success(self):
        """Send GET request for 'available' status and assert response 200 and response length bigger than 1"""
        # arrange & action
        response = self.get_find_pet_by_status(Status.available)

        # assert
        self.assertTrue(len(response.json()) >= 1)
        self.assertEqual(200, response.status_code)

    def test_find_pet_by_sold_status_success(self):
        """Send GET request for 'sold' status and assert response 200 and response length bigger than 1"""
        # arrange & action
        response = self.get_find_pet_by_status(Status.sold)

        # assert
        self.assertTrue(len(response.json()) >= 1)
        self.assertEqual(200, response.status_code)

    def test_find_pet_by_pending_status_success(self):
        """Send GET request for 'pending' status and assert response 200 and response length bigger than 1"""
        # arrange & action
        response = self.get_find_pet_by_status(Status.pending)

        # assert
        self.assertTrue(len(response.json()) >= 1)
        self.assertEqual(200, response.status_code)

    def test_delete_pet(self):
        """Send a POST request to create a new pet, Send DELETE request and assert it has been successfully deleted"""
        # arrange
        pet_info = self.__create_a_pet()

        # action
        delete_response = self.delete_pet_by_id(pet_info["id"])

        # assert
        self.assertEqual(delete_response.code, 200)
        self.assertEqual(delete_response.message, str(pet_info["id"]))
        self.assertEqual(delete_response.type, "unknown")

    def test_update_pet(self):
        """Creates a new pet using POST request, update it and assert that name is equal to test with GET request."""
        # arrange
        pet_info: dict = helper.build_new_pet_payload()
        payload: Pet = helper.get_new_pet_payload(name=pet_info["name"], photoUrls=pet_info["photoUrls"], status=pet_info["status"], id_=pet_info["id"])
        self.post_add_new_pet(payload)
        payload_post_update: Pet = helper.rebuild_pet_payload(initial_payload=payload, name="test")

        # action
        self.put_update_existing_pet(payload_post_update)

        # assert
        res: PetMetaData = self.get_find_pet_by_id(payload.id)
        self.assertEqual(res.pet.name, "test")

    def test_delete_pet_invalid(self):
        """Send DELETE request using invalid pet id, expect 404 code to return"""
        # arrange
        invalid_pet: int = random_functions.get_random_number(15)

        # action
        delete_response = self.delete_pet_by_id(invalid_pet)

        # assert
        self.assertEqual(delete_response, 404)

    def test_createPet_updateFormData_success(self):
        """Creates a generic pet, updates with formData its status and name, assert it has successfully changed."""
        # arrange
        data = {"name": random_functions.get_random_string(5), "status": random_functions.get_random_string(10)}
        pet_info = self.__create_a_pet()
        get_details_pre_change: PetMetaData = super().get_find_pet_by_id(pet_info["id"])

        # action
        update_details: ApiResponse = super().post_update_pet_form_data(pet_info["id"], data=data, is_form_data=True)

        # assert
        self.assertNotEqual(get_details_pre_change.pet.name, data["name"])
        self.assertNotEqual(get_details_pre_change.pet.status, data["status"])
        self.assertEqual(get_details_pre_change.pet.name, pet_info["name"])
        self.assertEqual(get_details_pre_change.pet.status, pet_info["status"])

        get_details_post_change: PetMetaDataCustomStatus = super().get_find_pet_by_id(pet_info["id"])

        self.assertNotEqual(get_details_post_change.pet.name, pet_info["name"])
        self.assertNotEqual(get_details_post_change.pet.status, pet_info["status"])

        self.assertEqual(pet_info["id"], int(update_details.message))
        self.assertEqual(get_details_post_change.pet.name, data["name"])
        self.assertEqual(get_details_post_change.pet.status, data["status"])

    # ---------------------------------------------------Class Methods--------------------------------------------------

    def __create_a_pet(self) -> dict:
        """Builds a generic pet object and sends a POST request with that object"""
        pet_info: dict = helper.build_new_pet_payload()
        payload: Pet = helper.get_new_pet_payload(name=pet_info["name"], photoUrls=pet_info["photoUrls"], status=pet_info["status"], id_=pet_info["id"])
        self.post_add_new_pet(payload)
        return pet_info
