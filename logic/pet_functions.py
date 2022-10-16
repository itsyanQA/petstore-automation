from random import randint, random, choice
from helper import random_functions
from models.enum.Status import Status
from models.request.Pet import Pet


def build_new_pet_payload(id_: int = None, name: str = None, photoUrls: list[str] = None, status: Status = None) -> dict:
    """Builds the nessaccary data for the pet object"""
    if id_ is not None:
        id_ = id_
    else:
        id_: int = random_functions.get_random_number(randint(1, 9))

    if name is not None:
        name = name
    else:
        name: str = random_functions.get_random_string(randint(1, 9))

    if photoUrls is not None:
        photoUrls = photoUrls
    else:
        photoUrls: list[str] = [random_functions.get_random_string(randint(1, 9))]

    if status is not None:
        status = status
    else:
        status: Status = choice(list(Status))
    return {"id": id_, "name": name, "photoUrls": photoUrls, "status": status}


def rebuild_pet_payload(initial_payload: Pet, id_: int = None, name: str = None, photoUrls: list[str] = None, status: Status = None) -> Pet:
    """Takes the existing pet object and updates it to our needs, returns the updated payload"""
    update_payload: Pet = initial_payload
    if id_ is not None:
        update_payload.id = id_
    elif name is not None:
        update_payload.name = name
    elif photoUrls is not None:
        update_payload.photoUrls = photoUrls
    elif status is not None:
        update_payload.status = status
    return update_payload


def get_new_pet_payload(name: str, photoUrls: list[str], id_: int = None, category_id: int = None, category_name: str = None, tags_id: int = None, tags_name: str = None, status: Status = None) -> Pet:
    """Simply assigns the data to the pet object and returns it."""
    return Pet(id=id_, category_id=category_id, category_name=category_name, name=name, photoUrls=photoUrls, tags_id=tags_id, tags_name=tags_name, status=status)
