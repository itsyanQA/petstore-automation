from pydantic import BaseModel

from models.enum.User import User


class UserMetaData(BaseModel):
    user: User
    status_code: int
