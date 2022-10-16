from pydantic import BaseModel


class User(BaseModel):
    id: int = None
    username: str = None
    firstName: str = None
    lastName: str = None
    email: str = None
    password: str = None
    phone: str = None
    userStatus: int = None