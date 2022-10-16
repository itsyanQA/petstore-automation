from models.enum.User import User
from helper import random_functions
from random import randint


def build_user_object(id_: int = None, username: str = None, firstName: str = None, lastName: str = None, email: str = None, password: str = None, phone: str = None, userStatus: int = None, is_custom: bool = False) -> User:
    """Builds the user object and returns it"""
    user = User()
    user.id = random_functions.get_random_number(randint(7, 9))
    user.username = random_functions.get_random_string(randint(4, 9))
    user.firstName = random_functions.get_random_string(randint(2, 9))
    user.lastName = random_functions.get_random_string(randint(2, 9))
    user.email = random_functions.get_random_string(randint(2, 9))
    user.password = random_functions.get_random_string(9)
    user.phone = random_functions.get_random_string(randint(5, 9))
    user.userStatus = random_functions.get_random_number(randint(1, 9))
    args = {"id": id_, "username": username, "firstName": firstName, "lastName": lastName, "email": email, "password": password, "phone": phone, "userStatus": userStatus}
    for arg, value in args.items():
        if value is not None or value is None and is_custom:
            setattr(user, arg, value)
        else:
            pass
    else:
        return user

