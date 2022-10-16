import random
import string


def get_random_number(number_length: int) -> int:
    """Returns a random number with the length of specified in the parameter"""
    number: str = ""
    for len_ in range(0, number_length):
        rand_num = random.randint(0, 9)
        number += str(rand_num)
    return int(number)


def get_random_string(string_length: int) -> str:
    """Returns a random string with the length of specified in the parameter"""
    letters = string.ascii_lowercase
    result_str = "".join(random.choice(letters) for letter in range(string_length))
    return result_str

