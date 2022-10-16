from pydantic import BaseModel
from models.request.Pet import CustomStatusPet


class PetMetaDataCustomStatus(BaseModel):
    pet: CustomStatusPet
    status_code: int
