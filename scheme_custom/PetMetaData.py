from pydantic import BaseModel

from models.request.Pet import Pet


class PetMetaData(BaseModel):
    pet: Pet
    status_code: int
