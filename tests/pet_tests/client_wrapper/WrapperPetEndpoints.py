from typing import Union
from models.request.Pet import Pet
from tests.pet_tests.client.PetEndpoints import PetEndpoints


class WrapperPetEndpoints(PetEndpoints):
    def get_find_pet_by_status(self, status: str):
        return super().get_find_pet_by_status(status)

    def get_find_pet_by_id(self, pet_id: int) -> dict[str: Pet, str, int]:
        return super().get_find_pet_by_id(pet_id)

    def post_add_new_pet(self, body: Union[Pet, dict]):
        return super().post_add_new_pet(body)

    def delete_pet_by_id(self, pet_id: int):
        return super().delete_pet_by_id(pet_id)

    def put_update_existing_pet(self, body: Pet):
        return super().put_update_existing_pet(body)
